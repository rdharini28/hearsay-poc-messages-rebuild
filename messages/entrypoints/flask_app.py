
import os
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__, instance_relative_config=True)


from messages import bootstrap, views

bus = bootstrap.bootstrap()

@app.route("/messages/<message_id>", methods=["GET"])
def get_messages(message_id):
    result = views.get_message(message_id, bus.uow)
    if not result:
        return "not found", 404
    return jsonify(result), 200