from flask import jsonify
from flightfinder.models.flight_quote import FlightQuote


def process_response(api_response):
    quotes = api_response["Quotes"]
    places = api_response["Places"]
    carriers = api_response["Carriers"]

    results = []

    for quote in quotes:
        # Price capped at 40 GBP one way, and only direct flights
        if quote["MinPrice"] > 40.00 or not quote["Direct"]:
            continue
        for place in places:
            if place["PlaceId"] == quote["OutboundLeg"]["DestinationId"]:
                quote["OutboundLeg"]["DestinationId"] = place["Name"]
                break
        for carrier in carriers:
            if carrier["CarrierId"] in quote["OutboundLeg"]["CarrierIds"]:
                quote["OutboundLeg"]["CarrierIds"] = carrier["Name"]
                break

        results.append(
            FlightQuote(
                quote["OutboundLeg"]["DestinationId"],
                quote["MinPrice"],
                quote["OutboundLeg"]["DepartureDate"],
                quote["OutboundLeg"]["CarrierIds"],
            )
        )

    return jsonify(quotes=[e.to_json() for e in results])
