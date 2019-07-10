from json import load
from flask import render_template, Blueprint
from flightfinder.services import data_service

controller = Blueprint('controller', __name__)


@controller.route("/", methods=["GET"])
def landing_page():
    return render_template("index.html")


@controller.route("/destinations", methods=["GET"])
def destinations_data():
    # response = api_service.request()
    response = load(open("flightfinder/mocks/data.json"))
    results = data_service.process_response(response)
    return results
