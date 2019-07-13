class FlightQuote:
    destination_airport = ""
    destination_country = ""
    price = 0.00
    date_outbound = ""
    date_inbound = ""
    carrier_outbound = ""
    carrier_inbound = ""

    def __init__(
        self,
        destination_airport,
        destination_country,
        price,
        date_outbound,
        date_inbound,
        carrier_outbound,
        carrier_inbound,
    ):
        self.destination_airport = destination_airport
        self.destination_country = destination_country
        self.price = price
        self.date_outbound = date_outbound
        self.date_inbound = date_inbound
        self.carrier_outbound = carrier_outbound
        self.carrier_inbound = carrier_inbound

    def to_json(self):
        return {
            "destination": self.destination_airport,
            "country": self.destination_country,
            "price": self.price,
            "dateOutbound": self.date_outbound,
            "dateInbound": self.date_inbound,
            "carrierOutbound": self.carrier_outbound,
            "carrierInbound": self.carrier_inbound,
        }
