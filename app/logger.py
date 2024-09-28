import logging
import os

from time import time
from logging.handlers import RotatingFileHandler
from flask import request


def setup_logging(app):
    # create log folder
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # create file handler
    file_handler = RotatingFileHandler('logs/flask.log', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    file_handler.setLevel(logging.INFO)

    # add handler to app
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('App startup')


    # before request set start_time
    @app.before_request
    def start_timer():
        request.start_time = time()


    # after request write log
    @app.after_request
    def log_request(response):
        duration = time() - request.start_time
        status = response.status_code
        app.logger.info(f'[{request.method}] {request.url} (in {duration:.4f}s)')
        return response
