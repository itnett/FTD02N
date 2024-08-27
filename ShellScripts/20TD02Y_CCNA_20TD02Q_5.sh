shell
   configure terminal
   ip dhcp pool VLAN10
   network 192.168.10.0 255.255.255.0
   default-router 192.168.10.1
   dns-server 8.8.8.8
   exit