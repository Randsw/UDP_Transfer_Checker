import socket
import time
import os


class Transmitter:
    """
    Transmitter Class
    self.port - UDP port
    self.filename - path to file wish to send
    self.ip - destination ip
    self.buff_size - payload data size in UDP datagram

    method send() - send file to specified IP, port and with selected buffer_size
    """

    def __init__(self, ip, filename, buff_size=8950, port=37777):
        self.port = port
        self.ip = ip
        self.buff_size = buff_size
        self.filename = filename

    def send(self, queue=None):
        addr = (self.ip, self.port)
        transm = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            transm.connect(addr)
        except ConnectionRefusedError:
            transm.close()
            raise ConnectionRefusedError
        file_length = os.path.getsize(self.filename)
        datagram = os.path.basename(self.filename).encode('utf-8') + file_length.to_bytes(4, byteorder='big',
                                                                                          signed=False)
        transm.sendto(datagram, addr)
        time.sleep(0.001)
        datagram_count = 0
        with open(self.filename, 'rb') as f:
            send_data = f.read(self.buff_size)
            while send_data:
                time.sleep(0.00000001)
                transm.sendto(send_data, addr)
                datagram_count += 1
                queue.put(datagram_count)
                send_data = f.read(self.buff_size)
        transm.close()
