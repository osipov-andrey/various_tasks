'''
solution without using dependencies, only UDP but mostly
'''
# !/usr/bin/env python

import datetime
import struct
import time
from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
import threading

NTP_PACKET_FORMAT = "!12I"
NTP_DELTA = (datetime.date(1970, 1, 1) - datetime.date(1900, 1, 1)).days * 24 * 3600  # 1970-01-01 00:00:00  # python3
# NTP_DELTA = 2208988800L  # python 2
NTP_QUERY = '\x1b' + 47 * '\0'
NTP_QUERY = NTP_QUERY.encode('utf-8')  # python3


# method adds fractions of seconds to the implementation and closes the socket properly
def ntp_time(host="pool.ntp.org", port=123):
    with closing(socket(AF_INET, SOCK_DGRAM)) as s:
        s.sendto(NTP_QUERY, (host, port))
        msg, address = s.recvfrom(1024)

    unpacked = struct.unpack(NTP_PACKET_FORMAT, msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
    return unpacked[10] + float(unpacked[11]) / 2 ** 32 - NTP_DELTA


def current_time_print():
    while True:
        current_time = time.ctime(ntp_time()).replace("  ", " ")
        print(current_time)
        time.sleep(5)


thread = threading.Thread(target=current_time_print, args=())
thread.start()

sock = socket(AF_INET, SOCK_DGRAM)
server_address = '127.0.0.1'
server_port = 8888
server = (server_address, server_port)
sock.bind(server)


def NTP_UDP():
    while True:
        comand, client_address = sock.recvfrom(1024)
        if comand == b'Get time':
            current_time = time.ctime(ntp_time()).replace("  ", " ")
            sent = sock.sendto(current_time.encode('utf-8'), client_address)
            print(f"Echoing Current Time {current_time} back to " + str(client_address))

    sock.close()


thread = threading.Thread(target=NTP_UDP, args=())
thread.start()