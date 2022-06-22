import smtplib
from flask import request, render_template
from redis_utils import *

def mail_send(email):
    secret_code = key()
    confirm_url = f'localhost:5000/verify_email?key={secret_code}'
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    html = render_template('mail.html', confirm_url=confirm_url)
    mail.login("nsardra@gmail.com", "vibha@aravindamnew")
    mail.sendmail("nsardra@gmail.com", email, html)
    mail.quit()