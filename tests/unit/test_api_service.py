import unittest
from json import load
from flask import Flask
from flightfinder.services import api_service

app = Flask(__name__)


class TestAPIService(unittest.TestCase):
    mock_data = "flightfinder/mock/data.json"

    def test_url_error_handler(self):
        with app.app_context():
            mock_external_response = {"message": "API doesn't exists"}
            expected_internal_response = {
                "errorMessage": "Tell the repo author that the url has changed for this API"
            }
            self.assertEqual(
                expected_internal_response,
                api_service.check_data_errors(mock_external_response).json,
            )

    def test_header_key_error_handler(self):
        with app.app_context():
            mock_external_response = {
                "message": "Missing RapidAPI application key. Go to "
                "https://docs.rapidapi.com/docs/keys to learn how to get your API "
                "application key."
            }
            expected_internal_response = {
                "errorMessage": "Tell the repo author that the application key is no longer "
                "valid"
            }
            self.assertEqual(
                expected_internal_response,
                api_service.check_data_errors(mock_external_response).json,
            )

    def test_unknown_error_handler(self):
        with app.app_context():
            mock_external_response = {"message": "Any other possible error"}
            expected_internal_response = {
                "errorMessage": "Unknown error, please alert the repo author"
            }
            self.assertEqual(
                expected_internal_response,
                api_service.check_data_errors(mock_external_response).json,
            )

    def test_no_error_handler(self):
        with app.app_context():
            mock_external_response = {"data": "response data"}
            expected_internal_response = False
            self.assertEqual(
                expected_internal_response,
                api_service.check_data_errors(mock_external_response),
            )

    def test_quote_length(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual(5, len(results["quotes"]))

    def test_quote_content_carrier(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual("Ryanair", results["quotes"][0]["carrierInbound"])
                self.assertEqual("Ryanair", results["quotes"][1]["carrierOutbound"])

    def test_quote_content_country(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual("Ireland", results["quotes"][1]["country"])
                self.assertEqual("France", results["quotes"][2]["country"])

    def test_quote_content_date(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual(
                    "2019-07-30T00:00:00", results["quotes"][3]["dateInbound"]
                )
                self.assertEqual(
                    "2019-07-21T00:00:00", results["quotes"][4]["dateOutbound"]
                )

    def test_quote_content_destination(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual("Girona", results["quotes"][0]["destination"])
                self.assertEqual(
                    "Ireland West Airport Knock", results["quotes"][1]["destination"]
                )

    def test_quote_content_price(self):
        with app.app_context():
            with open(self.mock_data, "r") as f:
                results = api_service.process_response([load(f)]).json
                self.assertEqual(30.0, results["quotes"][1]["price"])
                self.assertEqual(72.0, results["quotes"][2]["price"])
