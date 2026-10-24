#!/usr/bin/env python3
"""IPv4/IPv6 subnet calculator using Python's standard ipaddress module."""
import ipaddress


def main():
    value = input("Enter IP address with prefix (example 192.168.1.10/24): ").strip()
    try:
        network = ipaddress.ip_network(value, strict=False)
    except ValueError as exc:
        print(f"Invalid IP/prefix: {exc}")
        return
    print(f"Network:       {network.network_address}")
    print(f"Netmask:       {network.netmask}")
    print(f"Broadcast:     {getattr(network, 'broadcast_address', 'not applicable for IPv6')}")
    print(f"Prefix length: {network.prefixlen}")
    print(f"Total addresses: {network.num_addresses}")
    if network.version == 4 and network.num_addresses > 2:
        print(f"Usable hosts:  {network.num_addresses - 2}")
    elif network.version == 4:
        print("Usable hosts:  0 (network too small for conventional host addressing)")
    else:
        print("IP version:    IPv6")


if __name__ == "__main__":
    main()
