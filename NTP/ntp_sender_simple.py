'''
Takes current time from NTP-server and works in two threads:
    1) Printing current time 1 time in 5 seconds;
    2) Starting UDP-server and sending current time like string to clients.
'''
# !/usr/bin/env python

import datetime
import struct
import time
from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
import threading


# method adds fractions of seconds to the implementation and closes the socket properly
def ntp_time(host="pool.ntp.org", port=123):
    ntp_packet_format = "!12I"
    ntp_delta = (datetime.date(1970, 1, 1) - datetime.date(1900, 1,
                                                           1)).days * 24 * 3600  # 1970-01-01 00:00:00  # python3
    # ntp_delta = 2208988800L  # python 2
    ntp_query = '\x1b' + 47 * '\0'
    ntp_query = ntp_query.encode('utf-8')  # python3

    with closing(socket(AF_INET, SOCK_DGRAM)) as s:
        s.sendto(ntp_query, (host, port))
        msg, address = s.recvfrom(1024)

    unpacked = struct.unpack(ntp_packet_format, msg[0:struct.calcsize(ntp_packet_format)])
    return unpacked[10] + float(unpacked[11]) / 2 ** 32 - ntp_delta


def current_time_print():
    while True:
        current_time = time.ctime(ntp_time()).replace("  ", " ")
        print(current_time)
        time.sleep(5)


def time_sender_udp(host='127.0.0.1', port=8888):
    with closing(socket(AF_INET, SOCK_DGRAM)) as sock:
        server = (host, port)
        sock.bind(server)
        while True:
            comand, client_address = sock.recvfrom(1024)
            if comand == b'Get time':
                current_time = time.ctime(ntp_time()).replace("  ", " ")
                sent = sock.sendto(current_time.encode('utf-8'), client_address)
                print(f"Echoing Current Time {current_time} back to " + str(client_address))


def main():
    thread_a = threading.Thread(target=current_time_print, args=())
    thread_a.start()
    thread_b = threading.Thread(target=time_sender_udp, args=())
    thread_b.start()


if __name__ == '__main__':
    main()