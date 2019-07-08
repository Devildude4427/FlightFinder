from json import load

data_file = load(open("server/data/data.json"))


def process_response():
    quotes = data_file['Quotes']
    places = data_file['Places']
    carriers = data_file['Carriers']

    for quote in quotes:
        if quote['MinPrice'] > 40.00:
            continue
        for place in places:
            if place['PlaceId'] == quote['OutboundLeg']['DestinationId']:
                quote['OutboundLeg']['DestinationId'] = place['Name']
                print(quote['OutboundLeg']['DestinationId'])

    # for x in places:
    #     if x['PlaceId'] == 42795:
    #         print(x['IataCode'])
    #         print(x['Name'])
