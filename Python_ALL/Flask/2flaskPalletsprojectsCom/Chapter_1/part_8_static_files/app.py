from flask import Flask, url_for

app = Flask(__name__)

url_for('static', filename='style.css')