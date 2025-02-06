# pcap-generator

Script to generate a PCAP file with a single packet for testing network scenarios
using tcpreplay. This can be used for:

- Storm control tests (e.g., broadcast or multicast storms)
- Split-horizon tests (verifying from which port a MAC originates)
- Static MAC tests (ensuring a particular MAC is learned from a specific source)

The packet parameters are hardcoded below. You can change these to suit your testing needs.

Examples:
    - For broadcast storm control: set dst_mac = "ff:ff:ff:ff:ff:ff"
    - For multicast storm control: set dst_mac = "01:00:5e:12:34:56"
    - For unicast tests, use a unicast destination MAC (e.g., "00:aa:bb:cc:dd:ee")
    - To test split-horizon behavior, experiment with different source MACs
    - For static MAC tests, ensure that the source MAC is configured statically on your device

This script uses Scapy to construct the packet and then writes it directly to a PCAP file.
