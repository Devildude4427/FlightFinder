from server.domain.form_data import FormData
import urllib.request
from flask import Flask, render_template, request

server = Flask(
    __name__, static_folder="../static", template_folder="../templates"
)


def run_server():
    server.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)


@server.route("/", methods=["GET"])
def landing_page():
    return render_template("landing.html")


@server.route("/search", methods=["GET"])
def search_page():
    return render_template("search.html")


@server.route("/photon", methods=["GET"])
def tailwind_page():
    return render_template("photon.html")


@server.route("/search", methods=["POST"])
def search_flights():
    form = FormData(
        request.form.get("departureLocation"),
        request.form.get("dateOutbound"),
        request.form.get("earliestTimeOutbound"),
        request.form.get("dateInbound"),
        request.form.get("earliestTimeInbound"),
    )
    return "hello"


def create_api_request(form_data):
    api_request = urllib.request.Request(
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/"
        + "BRS-sky/anywhere/2019-09-01?inboundpartialdate=2019-12-01"
    )
    api_request.add_header(
        "X-RapidAPI-Host", "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    )
    api_request.add_header(
        "X-RapidAPI-Key", "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95"
    )
    resp = urllib.request.urlopen(api_request)
    content = resp.read()
