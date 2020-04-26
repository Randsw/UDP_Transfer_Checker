
class Transmitter:

    def __init__(self, IP, filename, buff_size=8950, port=37777):
        self.port = port
        self.IP = IP
        self.buff_size = buff_size
        self.filename = filename


