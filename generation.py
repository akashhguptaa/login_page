import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
secret_key = os.urandom(24)
print(secret_key)

app.secret_key = os.getenv('SECRET_KEY')
print(app.secret_key)

app.config['MYSQL_HOST'] = 'root'

load_dotenv()
app.config['MYSQL_PASSWORD'] = os.getenv('SQL_PASSWORD')
print(app.config['MYSQL_PASSWORD'])
app.config['MYSQL_DB'] = 'akash_login'
