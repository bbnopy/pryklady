from flask import Flask, app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! I'm using Flask."