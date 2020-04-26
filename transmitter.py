
class Transmitter:

    def __init__(self, ip, filename, buff_size=8950, port=37777):
        self.port = port
        self.ip = ip
        self.buff_size = buff_size
        self.filename = filename

    def send(self):
        pass
