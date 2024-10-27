import os
from urllib.parse import quote_plus

# Replace 'your_username', 'your_password', 'host', and 'port' with your actual credentials and host information
username = os.environ.get('MONGO_DB_USERNAME')
password = os.environ.get('MONGO_DB_PASSWORD')
host = os.environ.get('MONGO_DB_HOST')
port = os.environ.get('MONGO_DB_PORT')

encoded_password = quote_plus(password)

# Construct the MongoDB URI
connection_string = f'mongodb://{username}:{encoded_password}@{host}:{port}'
database_name="nlu"
collection_name="chat_history"
