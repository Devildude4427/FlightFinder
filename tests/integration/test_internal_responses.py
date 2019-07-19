import unittest
from datetime import datetime
from flask import Flask
from flightfinder.services import api_service


app = Flask(__name__)


class TestInternalResponses(unittest.TestCase):
    request_data = {
        "portOutbound": "BRS-sky",
        "country": "UK",
        "currency": "GBP",
        "locale": "en-GB",
    }
    results = ""

    def setUp(self):
        with app.app_context():
            self.results = api_service.request(self.request_data).json

    def test_quote_length(self):
        with app.app_context():
            self.assertLess(0, len(self.results["quotes"]))

    def test_quote_price_data(self):
        with app.app_context():
            self.assertIsInstance(self.results["quotes"][0]["price"], float)

    def test_quote_carrier_data(self):
        with app.app_context():
            self.assertIsInstance(self.results["quotes"][0]["carrierOutbound"], str)
            self.assertIsInstance(self.results["quotes"][0]["carrierInbound"], str)

    def test_quote_destination_data(self):
        with app.app_context():
            self.assertIsInstance(self.results["quotes"][0]["country"], str)
            self.assertIsInstance(self.results["quotes"][0]["destination"], str)

    def test_quote_date_data(self):
        with app.app_context():
            self.assertIsInstance(self.results["quotes"][0]["dateOutbound"], str)
            self.assertIsInstance(self.results["quotes"][0]["dateInbound"], str)
            date_format = "%Y-%m-%dT%H:%M:%S"
            outbound = datetime.strptime(
                self.results["quotes"][0]["dateOutbound"], date_format
            )
            self.assertGreater(outbound, datetime.now())
