import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    CONSUMER_KEY="AGl6fzEXGhIpQCsJxjHDaDuPxOORoZQp"
    CONSUMER_SECRET="dOoUfgj4o3sAISiG"
    SHORTCODE="999537"
    PASSKEY="26a8551bcd8191a39a341cf0509d1b348fd639cfb759b37924c67e97d65537cd"
    CALLBACK_URL="https://yourdomain.com/mpesa-callback"
    MPESA_BASE_URL = "https://api.safaricom.co.ke"

settings = Settings()

