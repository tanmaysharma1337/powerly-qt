import psutil
from datetime import datetime

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

if __name__ == "__main__":
    pass