class FlightQuote:
    destination_airport = ""
    destination_country = ""
    price = 0.00
    date_outbound = ""
    carrier = ""

    def __init__(self, destination_airport, destination_country, price, date_outbound, carrier):
        self.destination_airport = destination_airport
        self.destination_country = destination_country
        self.price = price
        self.date_outbound = date_outbound
        self.carrier = carrier

    def to_json(self):
        return {
            "destination": self.destination_airport,
            "country": self.destination_country,
            "price": self.price,
            "dateOutbound": self.date_outbound,
            "carrier": self.carrier,
        }
