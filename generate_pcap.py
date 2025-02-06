#!/usr/bin/env python3
from scapy.all import Ether, IP, TCP, Raw, wrpcap

# ========================================
# Packet parameters (modify as needed)
# ========================================

# Ethernet layer parameters
src_mac = "00:11:22:33:44:55"     # Source MAC address
# For testing storm control, you can use the following examples:
#   - Broadcast traffic: dst_mac = "ff:ff:ff:ff:ff:ff"
#   - Multicast traffic: dst_mac = "01:00:5e:12:34:56"
dst_mac = "ff:ff:ff:ff:ff:ff"     # Destination MAC address (broadcast)
eth_type = 0x0800                # Ethernet type for IP

# IP layer parameters
src_ip = "192.168.1.100"         # Source IP address
dst_ip = "192.168.1.255"         # Destination IP address (broadcast for storm control tests)
ip_ttl = 64                    # Time-to-live

# Transport layer parameters (TCP is used in this example; change to UDP if needed)
src_port = 12345
dst_port = 80

# Payload data (this can be any string or binary data)
payload = "Test packet for storm control, split-horizon, and static MAC testing."

# ========================================
# Construct the packet using Scapy
# ========================================

packet = (Ether(src=src_mac, dst=dst_mac, type=eth_type) /
          IP(src=src_ip, dst=dst_ip, ttl=ip_ttl) /
          TCP(sport=src_port, dport=dst_port) /
          Raw(load=payload))

# ========================================
# Write the packet to a PCAP file
# ========================================

pcap_filename = "test_packet.pcap"
wrpcap(pcap_filename, packet)

print(f"PCAP file '{pcap_filename}' generated successfully.")
