from flask import Flask, request, send_file, jsonify
import pytz
import json
import os
from datetime import datetime

app = Flask(__name__)

cet = pytz.timezone(os.getenv('TZ')) 

some_string = """
{ "ids"     : ["1", "2", "3"],
 "key"     : "eval{23W5865}",
  "context" : "restore" }
"""

@app.route('/', methods=['GET'])
def index():
    return send_file(path_or_file="var.env"), 200

@app.route('/ip', methods=['GET'])
def ip():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"Requester's IP: {ip_address}")
    return ip_address, 200

@app.route('/cet', methods=['POST'])
def get_cet():
    return str(datetime.now(cet))

@app.route("/get_turtle", methods=['GET'])
def get_turtle():
    returned_json = json.loads(some_string)
    return jsonify(returned_json), 200

@app.route("/super_secret", methods=['GET'])
def super_secret():
    if os.getenv('API_KEY'):
        return "access granted", 200
    else:
        return "access denied", 403