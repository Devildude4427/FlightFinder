import urllib.request


def request():
    response = urllib.request.urlopen(create_api_request())
    return response.read()


def create_api_request():
    api_request = urllib.request.Request(
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/"
        + "BRS-sky/anywhere/2019-09-01?inboundpartialdate=anytime"
    )
    api_request.add_header(
        "X-RapidAPI-Host", "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    )
    api_request.add_header(
        "X-RapidAPI-Key", "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95"
    )
    return api_request
