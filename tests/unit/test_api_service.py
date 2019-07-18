import unittest
from flask import Flask
from flightfinder.services import api_service

app = Flask(__name__)


class TestAPIService(unittest.TestCase):
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
