from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")


MALL_ID = os.getenv("MALL_ID")
STORE_ID = os.getenv("STORE_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
ID = os.getenv("ID")
PASSWORD = os.getenv("PASSWORD")
pass