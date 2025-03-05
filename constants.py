from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = "https://calc-be-1092.onrender.com"  # Updated to Render URL
PORT = os.getenv("PORT", "10000")

ENV = "production"  # Change from 'dev' to 'production' if needed

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure this is set in Render settings
