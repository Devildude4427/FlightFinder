import unittest
from flask import Flask
from flightfinder.services import api_service


app = Flask(__name__)


class TestExternalAPI(unittest.TestCase):
    """This tests the external API, and ensures the raw data still matches expectations"""

    request_data = {
        "portOutbound": "BRS-sky",
        "country": "UK",
        "currency": "GBP",
        "locale": "en-GB",
    }
    response = ""

    @classmethod
    def setUpClass(cls):
        with app.app_context():
            cls.response = api_service.create_api_request(cls.request_data).json()

    def test_api_response_for_errors(self):
        with app.app_context():
            data_errors = api_service.check_data_errors(self.response)
            self.assertFalse(data_errors)

    def test_quote_length(self):
        with app.app_context():
            self.assertGreater(len(self.response["Quotes"]), 0)

    def test_places_length(self):
        with app.app_context():
            self.assertGreater(len(self.response["Places"]), 0)

    def test_carriers_length(self):
        with app.app_context():
            self.assertGreater(len(self.response["Carriers"]), 0)

    def test_quote_price(self):
        with app.app_context():
            self.assertIsInstance(self.response["Quotes"][0]["MinPrice"], float)

    def test_quote_direct(self):
        with app.app_context():
            self.assertIsInstance(self.response["Quotes"][0]["Direct"], bool)

    def test_quote_carriers(self):
        with app.app_context():
            # Tests that carriers are still numbered keys, rather than string names
            self.assertIsInstance(
                self.response["Quotes"][0]["OutboundLeg"]["CarrierIds"][0], int
            )
            self.assertIsInstance(
                self.response["Quotes"][0]["InboundLeg"]["CarrierIds"][0], int
            )

    def test_quote_destinations(self):
        with app.app_context():
            self.assertIsInstance(
                self.response["Quotes"][0]["OutboundLeg"]["OriginId"], int
            )
            self.assertIsInstance(
                self.response["Quotes"][0]["OutboundLeg"]["DestinationId"], int
            )

            self.assertIsInstance(
                self.response["Quotes"][0]["InboundLeg"]["OriginId"], int
            )
            self.assertIsInstance(
                self.response["Quotes"][0]["InboundLeg"]["DestinationId"], int
            )

            # Tests that the information is still round-trip
            self.assertEqual(
                self.response["Quotes"][0]["OutboundLeg"]["OriginId"],
                self.response["Quotes"][0]["InboundLeg"]["DestinationId"],
            )
            self.assertEqual(
                self.response["Quotes"][0]["OutboundLeg"]["DestinationId"],
                self.response["Quotes"][0]["InboundLeg"]["OriginId"],
            )
