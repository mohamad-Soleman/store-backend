from flask import request
from app import flask_app

@flask_app.route("/")
def default():
    flask_app.logger.info({"request_path": request.path})
    return "hello world"