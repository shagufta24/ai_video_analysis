import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    UPLOAD_FOLDER = "uploads"
    DB_PATH = "database/transcripts.db"

# Ensure the upload folder exists
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
