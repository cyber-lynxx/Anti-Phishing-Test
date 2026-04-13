from flask import Flask, render_template, redirect
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
