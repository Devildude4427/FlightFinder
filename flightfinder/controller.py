import logging
from flask import render_template, Blueprint, request
from flightfinder.services import data_service, api_service

logger = logging.getLogger(__name__)
controller = Blueprint("controller", __name__)


@controller.route("/", methods=["GET"])
def landing_page():
    return render_template("index.html")


@controller.route("/getQuotes", methods=["POST"])
def destinations_data():
    if request.json:
        logger.info("Quote request received by server")
    response = api_service.request(request.json)
    logger.debug("API Response: " + response)
    results = data_service.process_response(response)
    return results
