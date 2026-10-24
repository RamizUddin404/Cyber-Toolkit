#!/usr/bin/env python3
"""Bounded TCP reachability check for a host you own or are authorized to test."""
import ipaddress
import socket


def validate_host(value):
    host = value.strip()
    if not host or len(host) > 253 or any(ch.isspace() for ch in host):
        raise ValueError("Enter a valid IP address or hostname.")
    try:
        return str(ipaddress.ip_address(host))
    except ValueError:
        if any(not part or len(part) > 63 for part in host.rstrip(".").split(".")):
            raise ValueError("Invalid hostname.")
        return host


def scan_ports(host, start_port, end_port, timeout=0.4):
    """Check at most 100 TCP ports sequentially with a short timeout."""
    host = validate_host(host)
    start_port, end_port = int(start_port), int(end_port)
    if not 1 <= start_port <= 65535 or not 1 <= end_port <= 65535:
        raise ValueError("Ports must be between 1 and 65535.")
    if end_port < start_port:
        raise ValueError("End port must be greater than or equal to start port.")
    if end_port - start_port + 1 > 100:
        raise ValueError("For safety, check at most 100 ports per run.")
    timeout = max(0.1, min(float(timeout), 0.8))
    open_ports = []
    checked = 0
    for port in range(start_port, end_port + 1):
        checked += 1
        try:
            with socket.create_connection((host, port), timeout=timeout):
                open_ports.append(port)
        except (OSError, TimeoutError):
            continue
    return {"host": host, "ports_checked": checked, "open_ports": open_ports,
            "note": "TCP reachability only; results depend on routing and firewall rules."}


def main():
    print("Bounded TCP Port Check")
    print("Only test systems you own or are explicitly authorized to assess.")
    host = input("Host/IP (default 127.0.0.1): ").strip() or "127.0.0.1"
    try:
        start = int(input("Start port (default 1): ").strip() or "1")
        end = int(input("End port (default 20): ").strip() or "20")
        if input("Type CHECK to continue: ").strip() != "CHECK":
            print("Cancelled.")
            return
        result = scan_ports(host, start, end)
    except (ValueError, OSError) as exc:
        print(f"Could not check ports: {exc}")
        return
    print(f"Host: {result['host']}")
    print(f"Ports checked: {result['ports_checked']}")
    print("Open ports: " + (", ".join(map(str, result["open_ports"])) if result["open_ports"] else "none detected"))


if __name__ == "__main__":
    main()
