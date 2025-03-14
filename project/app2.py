import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv("api_key.env")

GOOGLE_API_KEY = os.getenv("AIzaSyDJR3dTQjeZKTR3eiGiROtwMXCOuYSq1t4")
