class FlightQuote:
    destination = ""
    price = 0.00
    date_outbound = ""
    carrier = ""

    def __init__(self, destination, price, date_outbound, carrier):
        self.destination = destination
        self.price = price
        self.date_outbound = date_outbound
        self.carrier = carrier

    def to_json(self):
        return {
            "Destination": self.destination,
            "Price": self.price,
            "DateOutbound": self.date_outbound,
            "Carrier": self.carrier,
        }
