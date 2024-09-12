import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # CONSUMER_KEY="AGl6fzEXGhIpQCsJxjHDaDuPxOORoZQp"
    # CONSUMER_SECRET="dOoUfgj4o3sAISiG"
    # SHORTCODE="999537"
    # # PASSKEY="efa477b21f09a30aed4735658f4a35d736e24a7d53f3a61552501834fce70571"
    # PASSKEY="26a8551bcd8191a39a341cf0509d1b348fd639cfb759b37924c67e97d65537cd"
    # CALLBACK_URL="https://yourdomain.com/mpesa-callback"
    # MPESA_BASE_URL = "https://api.safaricom.co.ke"

    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    SHORTCODE = os.getenv("SHORTCODE")
    PASSKEY = os.getenv("PASSKEY")
    CALLBACK_URL = os.getenv("CALLBACK_URL")
    MPESA_BASE_URL = "https://api.safaricom.co.ke"

settings = Settings()

