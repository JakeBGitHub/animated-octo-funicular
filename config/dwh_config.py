import os
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DRIVER")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PASSWORD = os.getenv("PASSWORD")

SCHEDULED_QUERY = os.getenv("SCHEDULED_QUERY")
MANUAL_QUERY = os.getenv("MANUAL_QUERY")
