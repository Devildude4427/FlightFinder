from datetime import datetime
import requests
from flask import jsonify
from flightfinder.models.flight_quote import FlightQuote


def request(request_data):
    response = create_api_request(request_data).json()
    data_errors = check_data_errors(response)
    return data_errors if data_errors else process_response(response)


def check_data_errors(response):
    url_error = "API doesn't exists"  # "exists" is correct, external API made a typo
    header_key_error = (
        "Missing RapidAPI application key. Go to https://docs.rapidapi.com/docs/keys "
        "to learn how to get your API application key."
    )
    if "message" in response:
        if response["message"] == url_error:
            return jsonify(
                errorMessage="Tell the repo author that the url has changed for this API"
            )
        elif response["message"] == header_key_error:
            return jsonify(
                errorMessage="Tell the repo author that the application key is no longer valid"
            )
        else:
            return jsonify(errorMessage="Unknown error, please alert the repo author")
    return False


def create_api_request(request_data):
    # Temporary until date selection is implemented
    today = datetime.today()
    year_month = "{}-{}".format(today.year, "{:02d}".format(today.month))

    url = (
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/"
        + request_data["country"]
        + "/"
        + request_data["currency"]
        + "/"
        + request_data["locale"]
        + "/"
        + request_data["portOutbound"]
        + "/anywhere/"
        + year_month
        + "/"
        + year_month
    )
    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95",
    }

    return requests.get(url, headers=headers)


def process_response(api_response):
    quotes = api_response["Quotes"]
    places = api_response["Places"]
    carriers = api_response["Carriers"]

    results = []

    for quote in quotes:
        destination_airport = ""
        destination_country = ""
        carrier_outbound = ""
        carrier_inbound = ""

        # Price capped at 40 GBP one way, and only direct flights
        if quote["MinPrice"] > 100.00 or not quote["Direct"]:
            continue

        # TODO Origin place needs to be checked for city origins. "London" may be provided, but user needs to know
        #  which London airport the quote is for
        for place in places:
            if place["PlaceId"] == quote["OutboundLeg"]["DestinationId"]:
                destination_airport = place["Name"]
                destination_country = place["CountryName"]
                break
        for carrier in carriers:
            if carrier["CarrierId"] in quote["OutboundLeg"]["CarrierIds"]:
                carrier_outbound = carrier["Name"]
            if carrier["CarrierId"] in quote["InboundLeg"]["CarrierIds"]:
                carrier_inbound = carrier["Name"]
            if carrier_outbound and carrier_inbound:
                break

        results.append(
            FlightQuote(
                destination_airport,
                destination_country,
                quote["MinPrice"],
                quote["OutboundLeg"]["DepartureDate"],
                quote["InboundLeg"]["DepartureDate"],
                carrier_outbound,
                carrier_inbound,
            )
        )
    return jsonify(quotes=[e.to_json() for e in results])
