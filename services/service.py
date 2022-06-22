from models.model import *
import random, string
import os
import math
import smtplib
import re
import hashlib
from utils.mail_utils import *


def user_login(email, password):
    '''
    For verify the user and generate tokens
    :param username:
    :param password:
    :return: A dict which contains auth tokens
    '''
    user = match_credentials(email, password)
    if not user:
        raise Exception('Invalid email or password')
    access_token = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(128))
    refresh_token = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    status = insert_token(user["id"], access_token, refresh_token)
    if status:
        return {"access_token": access_token, "refresh_token": refresh_token}

def user_sign_up(name,email,password,confirm_password,dob):

    #users = users()
    # if email in users:
    #     raise Exception('email already in use')
    salt = os.urandom(32)
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.match(regex, email):
        raise Exception('not a valid email')
    hash_password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000,
        dklen=128
    )
    password = hash_password
    mail_send(email)
    registered = create_user(name, email, password, confirm_password, dob)
    if registered:
        return True










