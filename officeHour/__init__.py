from flask import Flask
from .env import KEY # if you use a separate env.py file

app = Flask(__name__)
# app.secret_key = KEY  # if you use a separate env.py file use this line
app.secret_key = "My super secret key"  # Otherwise keep this one