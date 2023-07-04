import databases
from dotenv import load_dotenv
import os

load_dotenv()
#conexion
DATABASE_URL = os.getenv('DATABASE_URL')

database = databases.Database(DATABASE_URL)
