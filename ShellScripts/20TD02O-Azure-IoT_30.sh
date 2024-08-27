bash
# Installer Mender klient på enheten
sudo apt-get install mender

# Konfigurer Mender klient
sudo vi /etc/mender/mender.conf
{
  "InventoryPollIntervalSeconds": 1800,
  "RetryPollIntervalSeconds": 300,
  "RootfsPartA": "/dev/mmcblk0p2",
  "RootfsPartB": "/dev/mmcblk0p3",
  "ServerURL": "https://mender-server-url"
}

# Start Mender klient
sudo systemctl start mender