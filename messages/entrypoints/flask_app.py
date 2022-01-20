
import os
from datetime import datetime
from flask import Flask, jsonify, request
from messages.service_layer import message_services, unit_of_work
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__, instance_relative_config=True)
get_session = unit_of_work.DEFAULT_SESSION_FACTORY

from messages import bootstrap, views

bus = bootstrap.bootstrap()

@app.route("/messages/<message_id>", methods=["GET"])
def get_messages(message_id):
    result = views.get_message(message_id, bus.uow)
    if not result:
        return "not found", 404
    return jsonify(result), 200

@app.route("/message/send", methods=["POST"])
def send_message():
    message_services.send_message(
        request.json["id"],
        request.json["name"],
        request.json["status"],
        datetime.now(),
        request.json["text"],
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201

## come back to this later.
if __name__ == '__main__':
    logger = logging.getLogger('werkzeug')
    handler = RotatingFileHandler('messages.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run()
