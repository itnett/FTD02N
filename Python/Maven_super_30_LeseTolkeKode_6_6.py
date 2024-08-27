python
import psutil

def monitor_virtual_machines():
    for vm in psutil.virtual_memory():
        print(f"Virtual Machine: {vm.name}")
        print(f"  CPU Usage: {vm.cpu_percent}%")
        print(f"  Memory Usage: {vm.memory_percent}%")
        print(f"  Disk Usage: {vm.disk_percent}%")
        print(f"  Network Usage: {vm.network_percent}%\n")

def main():
    print("Monitoring Virtual Machines on Hypervisor...\n")
    monitor_virtual_machines()



if __name__ == "__main__":
    main()