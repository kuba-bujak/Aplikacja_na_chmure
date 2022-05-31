from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

''' OBSŁUGA EMAIL'''

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
'''TRASOWANIE'''


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


'''OBSLUGA BLEDOW'''


@app.route('/error_denied')
def error_denied():
    abort(401)


@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505


@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response


@app.errorhandler(404)
def not_found_error():
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
