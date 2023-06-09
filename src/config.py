import os
from dotenv import load_dotenv


load_dotenv()

# DB parameters
DB_USER = os.environ.get('DB_USER')
DB_USER_PASSWORD = os.environ.get('DB_USER_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

# Auth parameters
SECRET_AUTH = os.environ.get("SECRET_AUTH")
