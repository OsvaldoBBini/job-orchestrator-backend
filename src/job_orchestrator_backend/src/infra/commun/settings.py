import os
from dotenv import load_dotenv

load_dotenv()

connection_url = os.getenv("DATABASE_URL")