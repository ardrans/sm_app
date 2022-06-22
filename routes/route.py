from flask import request, render_template
from flask import jsonify
import logging
import traceback

from utils.redis_utils import *
from services.service import *


def create_routes(app):
    @app.route('/login', methods=['POST'])
    def login():
        try:
            user_credentials = request.json
            email = user_credentials.get('email')
            password = user_credentials.get('password')
            if not email or not password:
                raise Exception('email or password is missing')
            token = user_login(email, password)
            return jsonify(
                {"success": True, "access_token": token.get('access_token'),
                 'refresh_token': token.get('refresh_token')})
        except Exception as e:
            logging.error('While logging, %s', e)
            return jsonify({"success": False, "message": e.args[0]})

    @app.route('/sign_up', methods=['POST'])
    def sign_up():
        try:
            user_details = request.json
            name = user_details.get('name')
            email = user_details.get('email')
            password = user_details.get('password')
            confirm_password = user_details.get('confirm_password')
            if not password == confirm_password:
                raise Exception('mismatch in password')
            dob = user_details.get('dob')
            if not name or not email or not password or not dob:
                raise Exception('required field is missing')
            user_sign_up(name, email, password, confirm_password, dob)
            if True:
                return jsonify({"success": True, "message": "You have successfully signed up"})

        except Exception as e:
            logging.error('While logging, %s', e)
            traceback.print_exc()
            return jsonify({"success": False, "message": e.args[0]})

    #
    # @app.route('/verify_email/<key>', methods=['POST'])
    # def verify_email():
    #     try:
    #         key = request.args.get('key')
    #         if not key:
    #             raise Exception('Key is missing')
    #
    #     except Exception as err:
    #         pass
