from flask import Flask
from flask_mail import Mail, Message
from flask import render_template

app = Flask(__name__)

app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'xanandra2014@gmail.com',
    MAIL_PASSWORD = 'Xanandra123',
)
 
mail = Mail(app)

@app.route('/')
def index():
    msg = Message(subject='Gracias por su inscripcion', sender='xanandra2014@gmail.com', recipients=['deynercatacora@upeu.edu.pe'], reply_to='webmaster@upeu.edu.pe')
    msg.body = "testing"
    msg.html = render_template('mail.html')
    mail.send(msg)
    return 'Enviado'

if __name__ == '__main__':
    app.run(debug=True)