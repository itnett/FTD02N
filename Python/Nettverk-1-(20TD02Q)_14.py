python
import subprocess

def scan_wifi():
    result = subprocess.run(['nmcli', '-f', 'SSID,SECURITY', 'dev', 'wifi'], capture_output=True, text=True)
    print(result.stdout)

scan_wifi()