import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/floodguard")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
