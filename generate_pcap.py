#!/usr/bin/env python3
from scapy.all import Ether, IP, TCP, Raw, ARP, wrpcap
import sys

# ========================================
# Packet parameters (modify as needed)
# ========================================

# Ethernet layer parameters
src_mac = "00:11:22:33:44:55"     # Source MAC address
dst_mac = "ff:ff:ff:ff:ff:ff"     # Destination MAC address (broadcast)
eth_type = 0x0800                # Ethernet type for IP (used for non-ARP packets)

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
# Parse command-line arguments
# ========================================
# Exclude the script name from the argument list
args = sys.argv[1:]
is_arp = False

if "-arp" in args:
    is_arp = True
    args.remove("-arp")

if len(args) > 0:
    pcap_filename = args[0]
else:
    pcap_filename = "packet.pcap"

# ========================================
# Construct the packet using Scapy
# ========================================
if is_arp:
    packet = (Ether(src=src_mac, dst=dst_mac) /
              ARP(op=1,
                  hwsrc=src_mac,
                  psrc=src_ip,
                  hwdst="00:00:00:00:00:00",
                  pdst=dst_ip))
else:
    packet = (Ether(src=src_mac, dst=dst_mac, type=eth_type) /
              IP(src=src_ip, dst=dst_ip, ttl=ip_ttl) /
              TCP(sport=src_port, dport=dst_port) /
              Raw(load=payload))

# ========================================
# Write the packet to a PCAP file
# ========================================
wrpcap(pcap_filename, packet)
print(f"PCAP file '{pcap_filename}' generated successfully.")
