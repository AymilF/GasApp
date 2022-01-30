# from flask import render_template, request, Blueprint, current_app
# import json
#
#
# from core.tasks import refresh_data
#
# APP_BLUEPRINT = Blueprint('app', __name__)
#
#
# @APP_BLUEPRINT.route("/",  methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         jsondata = refresh_data()
#         return render_template('gas.html', jsondata=jsondata)
#     else:
#         try:
#             with open('gas.json', 'r') as json_file:
#                 gasdata = json.load(json_file)
#                 current_app.logger.info(gasdata)
#                 return render_template('gas.html', jsondata=gasdata)
#         except FileNotFoundError:
#             return render_template('gas.html', jsondata={})


import os

import dash
import flask
import redis
from flask_sqlalchemy import SQLAlchemy
from rq import Queue

server = flask.Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///db/stations.db"
)
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)

app = dash.Dash(
    server=server,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://codepen.io/chriddyp/pen/bWLwgP.css"
    ]
)

# redis connection and RQ queue. use redistogo service when dpeloying to Heroku
redis_url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
conn = redis.from_url(redis_url)
queue = Queue(connection=conn)
