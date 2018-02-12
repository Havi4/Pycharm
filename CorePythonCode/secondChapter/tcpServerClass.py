from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('.....connected from : %s',self.client_address)
        st = ctime() + self.rfile.readline()
        self.wfile.write(st)
tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting to connection')
tcpServ.serve_forever()