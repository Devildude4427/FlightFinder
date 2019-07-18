# import unittest
# from flask import Flask
# from flightfinder.services import api_service
#
#
# app = Flask(__name__)
#
#
# class TestAPIResponse(unittest.TestCase):
#     # Arbitrary airport to get information from
#     request_data = {"portOutbound": "BRS-sky", "country": "UK", "currency": "GBP", "locale": "en-GB"}
#     results = api_service.request(request_data)
#
#     def test_quote_length(self):
#         with app.app_context():
#             self.assertGreater(len(self.results["Quotes"]), 0)
#
#     def test_places_length(self):
#         with app.app_context():
#             self.assertGreater(len(self.results["Places"]), 0)
#
#     def test_carriers_length(self):
#         with app.app_context():
#             self.assertGreater(len(self.results["Carriers"]), 0)
#
#     def test_quote_price(self):
#         with app.app_context():
#             self.assertIsInstance(self.results["Quotes"][0]["MinPrice"], float)
#
#     def test_quote_direct(self):
#         with app.app_context():
#             self.assertIsInstance(self.results["Quotes"][0]["Direct"], bool)
#
#     def test_quote_carriers(self):
#         with app.app_context():
#             # Tests that carriers are still numbered keys, rather than string names
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["OutboundLeg"]["CarrierIds"][0], int
#             )
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["InboundLeg"]["CarrierIds"][0], int
#             )
#
#     def test_quote_destinations(self):
#         with app.app_context():
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["OutboundLeg"]["OriginId"], int
#             )
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["OutboundLeg"]["DestinationId"], int
#             )
#
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["InboundLeg"]["OriginId"], int
#             )
#             self.assertIsInstance(
#                 self.results["Quotes"][0]["InboundLeg"]["DestinationId"], int
#             )
#
#             # Tests that the information is still round-trip
#             self.assertEqual(
#                 self.results["Quotes"][0]["OutboundLeg"]["OriginId"],
#                 self.results["Quotes"][0]["InboundLeg"]["DestinationId"],
#             )
#             self.assertEqual(
#                 self.results["Quotes"][0]["OutboundLeg"]["DestinationId"],
#                 self.results["Quotes"][0]["InboundLeg"]["OriginId"],
#             )
#
#     # TODO figure out how to test the dates
#     # TODO decide if rest of data should be tested, or just test to see if my code can handle response
#
#
# if __name__ == "__main__":
#     unittest.main()
