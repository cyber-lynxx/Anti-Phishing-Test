from flask import Flask, render_template, redirect
import os
api_key = os.getenv("API_KEY")

app = Flask(__name__, template_folder='.')

