import unittest
from json import load
from flask import Flask
from flightfinder.services.api_service import process_response


app = Flask(__name__)


class TestDataProcessing(unittest.TestCase):
    mock_data = "flightfinder/mock/data.json"

    def test_quote_length(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual(5, len(results["quotes"]))

    def test_quote_content_carrier(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual("Ryanair", results["quotes"][0]["carrierInbound"])
                self.assertEqual("Ryanair", results["quotes"][1]["carrierOutbound"])

    def test_quote_content_country(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual("Ireland", results["quotes"][1]["country"])
                self.assertEqual("France", results["quotes"][2]["country"])

    def test_quote_content_date(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual(
                    "2019-07-30T00:00:00", results["quotes"][3]["dateInbound"]
                )
                self.assertEqual(
                    "2019-07-21T00:00:00", results["quotes"][4]["dateOutbound"]
                )

    def test_quote_content_destination(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual("Girona", results["quotes"][0]["destination"])
                self.assertEqual(
                    "Ireland West Airport Knock", results["quotes"][1]["destination"]
                )

    def test_quote_content_price(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = process_response(load(f)).json
                self.assertEqual(30.0, results["quotes"][1]["price"])
                self.assertEqual(72.0, results["quotes"][2]["price"])


if __name__ == "__main__":
    unittest.main()
