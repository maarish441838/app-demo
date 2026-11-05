import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1 style='color:blue'>Hello from App Service v1 - This is my Test Branch or Area </h1><p>ENV: {os.environ.get('APP_ENV','not set')}</p>"