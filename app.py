from flask import Flask
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
	return "Flask installed!"
