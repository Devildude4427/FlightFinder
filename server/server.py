from flask import Flask, render_template, jsonify
from server.services import data_service, api_service

server = Flask(__name__, static_folder="../static", template_folder="../templates")


def run_server():
    server.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)


@server.route("/", methods=["GET"])
def landing_page():
    data_service.process_response()
    return render_template("index.html")


@server.route("/destinations", methods=["POST"])
def destinations_data():
    response = api_service.request()
    return jsonify("hello")
