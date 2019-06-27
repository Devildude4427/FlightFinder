class FormData:
    def __init__(
        self,
        departure_location,
        date_outbound,
        earliest_time_outbound,
        date_inbound,
        earliest_time_inbound,
    ):
        self.departure_location = departure_location
        self.date_outbound = date_outbound
        self.earliest_time_outbound = earliest_time_outbound
        self.date_inbound = date_inbound
        self.earliest_time_inbound = earliest_time_inbound
