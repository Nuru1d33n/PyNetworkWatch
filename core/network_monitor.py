from scapy.all import ARP, Ether, srp, sniff
from core.logger import Logger
from core.alert import AlertManager
import socket
import netifaces

class NetworkMonitor:
    def __init__(self, logger: Logger, alert_manager: AlertManager):
        self.logger = logger
        self.alert_manager = alert_manager
        self.device_list = set()

    def get_device_name(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return "Unknown"

    def get_network_ip_range(self):
        try:
            gateways = netifaces.gateways()
            gateway_ip = gateways['default'][netifaces.AF_INET][0]
            interface = 'wlan0'
            netmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            ip_parts = map(int, netmask.split('.'))
            bits = sum(bin(part).count('1') for part in ip_parts)
            return f"{gateway_ip}/{bits}"
        except (KeyError, IndexError, ValueError):
            return "192.168.0.1/24"

    def scan_network(self):
        ip_range = self.get_network_ip_range()
        print(f"Scanning network {ip_range}...")
        arp_request = ARP(pdst=ip_range)
        broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
        arp_request_broadcast = broadcast / arp_request
        answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        for element in answered_list:
            device_ip = element[1].psrc
            device_mac = element[1].hwsrc
            device_name = self.get_device_name(device_ip)
            device_identifier = (device_ip, device_mac)

            if device_identifier not in self.device_list:
                self.device_list.add(device_identifier)
                self.logger.log_device(device_ip, device_mac, device_name)
                print(f"Logged: IP {device_ip}, MAC {device_mac}, Name: {device_name}")

    def detect_device(self, packet):
        if packet.haslayer(ARP) and packet[ARP].op == 1:
            device_ip = packet[ARP].psrc
            device_mac = packet[ARP].hwsrc
            device_name = self.get_device_name(device_ip)
            device_identifier = (device_ip, device_mac)

            if device_identifier not in self.device_list:
                self.device_list.add(device_identifier)
                self.logger.log_device(device_ip, device_mac, device_name)
                self.alert_manager.send_alert(device_ip, device_mac)
                print(f"New device: IP {device_ip}, MAC {device_mac}, Name: {device_name}")

    def start_monitoring(self):
        self.scan_network()
        print("Starting live network monitoring...")
        sniff(prn=self.detect_device, filter="arp", store=0)
