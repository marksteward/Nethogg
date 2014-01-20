#!/usr/bin/env python
from dpkt import ethernet
import pcap
from socket import inet_ntoa
from collections import defaultdict


macs = defaultdict(int)
ips = defaultdict(int)

def process(ts, pkt):
    length = len(pkt)
    eth = ethernet.Ethernet(pkt)
    macs[eth.src] += length
    macs[eth.dst] += length
    if eth.type == ethernet.ETH_TYPE_IP:
        ip = eth.data
        ips[ip.src] += length
        ips[ip.dst] += length


def mac_ntoa(addr):
    return ':'.join('%02x' % ord(addr[i]) for i in range(6))

def dump_tables():

    print
    for k, v in macs.items():
        print mac_ntoa(k), v

    print
    for k, v in ips.items():
        print inet_ntoa(k), v


r = pcap.pcap(None, 65535, False, 500)
try:
    while True:
        r.dispatch(100, process)
        # ouptut the data somewhere

except KeyboardInterrupt:
    dump_tables()


