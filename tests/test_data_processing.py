import os
import sys
import unittest
from json import load
from flask import Flask

sys.path.append(os.getcwd())  # Hack to be able to run the tests from a terminal
from flightfinder.services import data_service  # noqa: E402


app = Flask(__name__)


class TestDataProcessingMethods(unittest.TestCase):
    mock_data = "flightfinder/mock/data.json"

    def test_quote_length(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(len(results["quotes"]), 5)

    def test_quote_content_carrier(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(results["quotes"][0]["carrierInbound"], "Ryanair")
                self.assertEqual(results["quotes"][1]["carrierOutbound"], "Ryanair")

    def test_quote_content_country(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(results["quotes"][1]["country"], "Ireland")
                self.assertEqual(results["quotes"][2]["country"], "France")

    def test_quote_content_date(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(
                    results["quotes"][3]["dateInbound"], "2019-07-30T00:00:00"
                )
                self.assertEqual(
                    results["quotes"][4]["dateOutbound"], "2019-07-21T00:00:00"
                )

    def test_quote_content_destination(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(results["quotes"][0]["destination"], "Girona")
                self.assertEqual(
                    results["quotes"][1]["destination"], "Ireland West Airport Knock"
                )

    def test_quote_content_price(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = data_service.process_response(load(f)).json
                self.assertEqual(results["quotes"][1]["price"], 30.0)
                self.assertEqual(results["quotes"][2]["price"], 72.0)


if __name__ == "__main__":
    unittest.main()
