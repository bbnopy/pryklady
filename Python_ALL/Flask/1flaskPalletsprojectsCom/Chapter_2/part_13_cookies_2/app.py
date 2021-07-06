from flask import Flask, make_response
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp