import socket
import time
import os


class Transmitter:

    def __init__(self, ip, filename, buff_size=8950, port=37777):
        self.port = port
        self.ip = ip
        self.buff_size = buff_size
        self.filename = filename

    def send(self):
        addr = (self.ip, self.port)
        transm = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #transm.connect(addr)
        file_length = os.path.getsize(self.filename)
        datagram = os.path.basename(self.filename).encode('utf-8') + file_length.to_bytes(4, byteorder='big', signed=False)
        transm.sendto(datagram, addr)
        time.sleep(0.001)
        with open(self.filename, 'rb') as f:
            send_data = f.read(self.buff_size)
            while send_data:
                time.sleep(0.00002)
                transm.sendto(send_data, addr)
                send_data = f.read(self.buff_size)
        transm.close()
