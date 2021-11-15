from flask import Flask
# from .env import KEY # if you use a separate env.py file

app = Flask(__name__)
# app.secret_key = KEY  # if you use a separate env.py file use this line
app.secret_key = "My super secret key"  # Otherwise keep this one


# alternate if python-dotenv is installed and using a .env file vs a env.py file
# from flask import Flask
# import os
# print( os.environ.get("API_KEY") )  # Use a line like this if using an api that requires a key

# app = Flask(__name__)
# app.secret_key = os.environ.get("KEY")  # this is the update toe the secret key if using .env file
