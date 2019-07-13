from flask import jsonify
from flightfinder.models.flight_quote import FlightQuote


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
                carrier_inbound
            )
        )

    return jsonify(quotes=[e.to_json() for e in results])
