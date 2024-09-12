from pydantic import BaseModel 

class STKPushRequest(BaseModel):
    phone_number:str
    amount: int