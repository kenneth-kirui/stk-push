from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import STKPushRequest
from app.mpesa import send_stk_push
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)




@app.get("/")
async def root():
    return{"message":"STK PUSH App is UP!"}

@app.post("/stk-push")
def initiate_stk_push(request:STKPushRequest):
    try:
        response = send_stk_push(request.phone_number, request.amount)
        return {"message":"STK Push initiated successfully", "data":response}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/mpesa-callback")
def mpesa_callback(data:dict):
    print("M-Pesa Callback Data:", data)
    try:
        stk_callback = data['Body']['stkCallback']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']

        if result_code == 0:
            # Successful transaction
            mpesa_receipt_number = stk_callback['CallbackMetadata']['Item'][1]['Value']
            phone_number = stk_callback['CallbackMetadata']['Item'][4]['Value']
            amount = stk_callback['CallbackMetadata']['Item'][0]['Value']

            print(f"Transaction Successful: {mpesa_receipt_number}, {phone_number}, {amount}")
        else:
            print(f"Transaction Failed: {result_desc}")
        
        return {"ResultCode": 0, "ResultDesc": "Success"}
    except Exception as e:
        return {"ResultCode": 1, "ResultDesc": f"Error: {str(e)}"}


