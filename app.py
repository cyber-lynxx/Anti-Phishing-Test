from flask import Flask, render_template, redirect, url_for
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__, template_folder='.')

@app.route("/")
def route_index():
  return redirect("index")

@app.route("/<name>")
def route(name):
    result = render_template(f"{name}.html")
    return result



if __name__ == "__main__":
    app.run()
