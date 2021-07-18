import os
from re import template
from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.evniron.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = ['Flasky']
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

def send_mail(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), know=session.get('know', False))