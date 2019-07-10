class FormData:
    def __init__(
        self,
        port_outbound,
        date_outbound,
        earliest_time_outbound,
        date_inbound,
        earliest_time_inbound,
    ):
        self.port_outbound = port_outbound
        self.date_outbound = date_outbound
        self.earliest_time_outbound = earliest_time_outbound
        self.date_inbound = date_inbound
        self.earliest_time_inbound = earliest_time_inbound
