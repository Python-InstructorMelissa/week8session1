from flask import Flask
import os
print( os.environ.get("API_KEY") )

app = Flask(__name__)
app.secret_key = os.environ.get("KEY")