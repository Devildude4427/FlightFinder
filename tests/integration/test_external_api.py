import unittest
from flask import Flask
from flightfinder.services.api_service import create_api_request


app = Flask(__name__)


class TestExternalAPI(unittest.TestCase):
    request_data = {
        "portOutbound": "BRS-sky",
        "country": "UK",
        "currency": "GBP",
        "locale": "en-GB",
    }
