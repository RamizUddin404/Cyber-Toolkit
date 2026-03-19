import socket

class PortScanner:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def scan_ports(self, start_port, end_port):
        open_ports = []
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((self.ip_address, port))
                if result == 0:
                    open_ports.append(port)
        return open_ports

if __name__ == '__main__':
    scanner = PortScanner('127.0.0.1')  # Example IP
    print(scanner.scan_ports(1, 100))  # Scan ports 1 to 100