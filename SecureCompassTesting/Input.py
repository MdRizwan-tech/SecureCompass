from flask import Flask
from os import environ

app = Flask(name)

Store the secret key in an environment variable
SECRET_KEY = environ.get('SECRET_KEY') # Retrieve the secret key from the environment variable

@app.route('/')
def index():
return "Welcome to the secure app!"

if name == 'main':
app.run(debug=True)
