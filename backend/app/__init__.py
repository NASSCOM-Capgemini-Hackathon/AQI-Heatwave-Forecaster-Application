import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
dotenv_path = os.path.dirname(os.path.abspath(__file__))+'\.env'
load_dotenv(dotenv_path)

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder='../templates',
            static_folder='../static')
app.config['SECRET_KEY'] = 'my secret key'
