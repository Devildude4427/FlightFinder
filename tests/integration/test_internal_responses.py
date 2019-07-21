import unittest
from json import load
from datetime import datetime
from flask import Flask
from flightfinder.services import api_service


app = Flask(__name__)


class TestInternalResponses(unittest.TestCase):
    """This tests the internal API, and ensures my services can still handle the expected json"""

    mock_data = "flightfinder/mock/data.json"
    request_data = {
        "portOutbound": "BRS-sky",
        "country": "UK",
        "currency": "GBP",
        "locale": "en-GB",
    }
    results = ""

    @classmethod
    def setUpClass(cls):
        with app.app_context():
            with open(cls.mock_data, "r") as f:
                cls.results = api_service.process_response([load(f)]).json

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
            # Simple date comparison, not worth much with mock data, but it's here anyways
            self.assertLess(outbound, datetime.now())
