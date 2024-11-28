import psutil
from datetime import datetime
import socket

# List all running processes
def list_processes():
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def get_system_boot_time():
    boot_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_timestamp)
    return boot_time
def get_current_ip():
    try:
        # Create a socket and connect to a public DNS server
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google Public DNS server
            return s.getsockname()[0]  # Get the IP address used in the connection
    except Exception as e:
        return None
if __name__ == "__main__":
    pass