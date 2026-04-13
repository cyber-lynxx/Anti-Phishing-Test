from flask import Flask
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/")
def go_to_index():
  return redirect("index.html")
