from flask import Flask, render_template, redirect
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def route(name):
    result = render_template(f"{name}.html")
    return result

if __name__ == "__main__":
    app.run()
