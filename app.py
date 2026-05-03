from flask import Flask, render_template, redirect, url_for
import os
from gen_email.py import generate_email

api_key = os.getenv("API_KEY")
app = Flask(__name__)

@app.route("/")
def route_index():
    return redirect("index")

@app.route("/favicon.ico")
def favicon():
    return "", 204

@app.route("/text")
def get_text():
    return generate_email(), 200, {"Content-Type": "text/plain"}

@app.route("/<name>")
def route(name):
    result = render_template(f"{name}.html")
    return result

if __name__ == "__main__":
    app.run()
