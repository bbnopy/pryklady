from flask import Flask
from flask.globals import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(f.filename)}")