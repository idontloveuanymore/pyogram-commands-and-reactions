import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

App_api_id = os.getenv('App_api_id')
App_api_hash = os.getenv('App_api_hash')
My_number = os.getenv('My_number')