bash
# Sikre passordfil i Linux
sudo chown root:root /etc/shadow
sudo chmod 600 /etc/shadow

# Sikre passordlagring i Windows
# Kjør i PowerShell som administrator
icacls "C:\Windows\System32\config\SAM" /inheritance:r
icacls "C:\Windows\System32\config\SAM" /grant:r Administrators:F
icacls "C:\Windows\System32\config\SAM" /deny Everyone:(F)