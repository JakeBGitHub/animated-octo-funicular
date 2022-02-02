import os
from dotenv import load_dotenv

load_dotenv()

DRIVER = os.getenv("DRIVER")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
UID = os.getenv("UID")
PASSWORD = os.getenv("PASSWORD")

A_QUERY = os.getenv("A_QUERY")
B_QUERY = os.getenv("B_QUERY")
