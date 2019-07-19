import logging
from flask import render_template, Blueprint, request
from flightfinder.services import api_service

logger = logging.getLogger(__name__)
controller = Blueprint("controller", __name__)


@controller.route("/", methods=["GET"])
def landing_page():
    return render_template("index.html")


@controller.route("/getQuotes", methods=["POST"])
def destinations_data():
    if request.json:
        logger.info("Quote request received by server")
    results = api_service.request(request.json)
    return results
