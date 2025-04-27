import socket
import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PortScanner:
    def __init__(self, ip, start_port, end_port, timeout=1.0):
        """
        Initialize the PortScanner with the target IP, port range, and timeout.

        :param ip: Target IP address to scan.
        :param start_port: Starting port number for the scan.
        :param end_port: Ending port number for the scan.
        :param timeout: Timeout for socket connections.
        """
        self.ip = ip
        self.start_port = start_port
        self.end_port = end_port
        self.timeout = timeout
        self.open_ports = []

    def scan_port(self, port):
        """
        Scan a single port on the target IP address.

        :param port: Port number to scan.
        :return: Tuple of (port, service) if open, else (None, None).
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)
            try:
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    service = self.get_service_name(port)
                    logging.info(f"Port {port} is open (Service: {service})")
                    return port, service
            except socket.error as e:
                logging.error(f"Socket error on port {port}: {e}")
            except Exception as e:
                logging.error(f"Error scanning port {port}: {e}")
        return None, None

    @staticmethod
    def get_service_name(port):
        """
        Get the service name for a given port number.

        :param port: Port number.
        :return: Service name or 'Unknown Service'.
        """
        try:
            return socket.getservbyport(port)
        except OSError:
            return "Unknown Service"

    def scan_ports(self):
        """
        Scan the range of ports on the target IP address using multithreading.

        :return: List of open ports and their services.
        """
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.scan_port, port): port for port in range(self.start_port, self.end_port + 1)}
            for future in futures:
                port, service = future.result()
                if port is not None:
                    self.open_ports.append((port, service))
        return self.open_ports

    def display_results(self):
        """
        Display the results of the port scan.
        """
        if self.open_ports:
            print("\nOpen ports found:")
            for port, service in self.open_ports:
                print(f"Port {port}: {service}")
        else:
            print("No open ports found.")

def main():
    """
    Main function to execute the port scanner.
    """
    print("Welcome to the Python Port Scanner!")
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    timeout = float(input("Enter the connection timeout (seconds): "))

    logging.info(f"Starting scan on {ip} from port {start_port} to {end_port} with a timeout of {timeout} seconds.")
    
    scanner = PortScanner(ip, start_port, end_port, timeout)
    
    start_time = time.time()
    open_ports = scanner.scan_ports()
    end_time = time.time()

    scanner.display_results()
    logging.info(f"Scan completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()

