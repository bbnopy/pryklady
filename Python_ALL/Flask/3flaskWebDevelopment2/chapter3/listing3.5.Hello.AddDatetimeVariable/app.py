from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())