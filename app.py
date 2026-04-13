from flask import Flask, render_template
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/")
def go_to_index():
  return redirect("/index")

@app.route("/<name>")
def route(name):
  return render_template(f"{name}.html")
