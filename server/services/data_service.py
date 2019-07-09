from json import load

data_file = load(open("server/data/data.json"))


def process_response():
    quotes = data_file["Quotes"]
    places = data_file["Places"]
    carriers = data_file["Carriers"]

    results = 0

    for quote in quotes:
        # Price capped at 40 GBP one way, and only direct flights
        if quote["MinPrice"] > 40.00 or not quote["Direct"]:
            continue
        results += 1
        for place in places:
            if place["PlaceId"] == quote["OutboundLeg"]["DestinationId"]:
                quote["OutboundLeg"]["DestinationId"] = place["Name"]
                break
        for carrier in carriers:
            if carrier["CarrierId"] in quote["OutboundLeg"]["CarrierIds"]:
                quote["OutboundLeg"]["CarrierIds"] = carrier["Name"]
                break

        print(
            "Quote Id: {}, Destinations: {}, Price: {}, Carrier: {}, Direct: {}".format(
                quote["QuoteId"],
                quote["OutboundLeg"]["DestinationId"],
                quote["MinPrice"],
                quote["OutboundLeg"]["CarrierIds"],
                quote["Direct"]
            )
        )

    print("The search came back with {} valid results".format(results))
