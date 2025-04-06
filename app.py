from dotenv import load_dotenv
import os
from flask import Flask, app

load_dotenv()
app = Flask(__name__)

# Getting environment variables
DEBUG = bool(os.getenv("DEBUG"))

@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=DEBUG)
