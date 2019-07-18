from datetime import datetime
import requests


def request(request_data):
    response = create_api_request(request_data)
    return response.json()


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
