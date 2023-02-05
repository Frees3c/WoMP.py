#!/usr/bin/env python3
# Wake on Magic Packet
# packet consits of: 6 bytes worth of ones in a row
# followed by the computers MAC address repeated 16 times

import socket

# Define the broadcast address
broadcast_addr = "255.255.255.255"

# Define the target port
port = 9999

# Define mac address
mac_address = "<CHANGE ME>"

# Define the packet data
packet = b"\xff\xff\xff\xff\xff\xff" + (mac_address * 16).encode()
print(packet)

# Create the UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the socket to broadcast mode and send
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto(packet, (broadcast_addr, port))
s.close()
