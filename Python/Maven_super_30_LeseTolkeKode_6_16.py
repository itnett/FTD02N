python
import psutil
import smtplib
from email.mime.text import MIMEText

def monitor_virtual_machines():
    """
    Overvåker ressursbruken til virtuelle maskiner og sender alarmer om nødvendig.
    """
    for vm in psutil.virtual_memory():
        cpu_usage = vm.cpu_percent()
        memory_usage = vm.memory_percent()

        print(f"Virtual Machine: {vm.name}")
        print(f"  CPU Usage: {cpu_usage}%")
        print(f"  Memory Usage: {memory_usage}%\n")

        # Sjekk om bruk overstiger terskelverdier
        if cpu_usage > 80 or memory_usage > 80:
            send_alarm_email(vm.name, cpu_usage, memory_usage)

def send_alarm_email(vm_name, cpu_usage, memory_usage):
    """
    Sender en e-postalarm hvis ressursbruken er for høy.
    """
    msg = MIMEText(f"Warning! {vm_name} is using {cpu_usage}% CPU and {memory_usage}% memory.")
    msg['Subject'] = f"High Resource Usage Alert for {vm_name}"
    msg['From'] = "monitor@yourcompany.com"
    msg['To'] = "admin@yourcompany.com"

    try:
        server = smtplib.SMTP('smtp.yourcompany.com')
        server.sendmail("monitor@yourcompany.com", ["admin@yourcompany.com"], msg.as_string())
        server.quit()
        print("Alert email sent.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")

def main():
    print("Monitoring Virtual Machines on Hypervisor...\n")
    monitor_virtual_machines()

if __name__ == "__main__":
    main()