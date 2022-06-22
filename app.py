
from flask import Flask
from flask_cors import CORS, cross_origin
from routes.route import *
app = Flask(__name__)

CORS(app)


if __name__ == "__main__":
    create_routes(app)
    app.run()