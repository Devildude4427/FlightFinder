import logging
from json import load
from flask import render_template, Blueprint, request
from flightfinder.services import data_service

logger = logging.getLogger(__name__)
controller = Blueprint("controller", __name__)


@controller.route("/", methods=["GET"])
def landing_page():
    return render_template("index.html")


@controller.route("/getQuotes", methods=["POST"])
def destinations_data():
    if request.data:
        logger.info("Request received by server")
    # response = api_service.request()
    response = load(open("flightfinder/mocks/newData.json"))
    results = data_service.process_response(response)
    return results
