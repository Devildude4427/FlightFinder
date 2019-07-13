import requests


def request(request_data):
    # response = urllib.request.urlopen(create_api_request(request_data))
    response = create_api_request(request_data)
    return response.json()


def create_api_request(request_data):
    url = (
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/UK/GBP/en-GB/"
        + request_data["portOutbound"]
        + "/anywhere/2019-07/2019-07"
    )
    headers = {
        "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95",
    }

    return requests.get(url, headers=headers)
