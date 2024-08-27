enable
   configure terminal
   hostname MyRouter
   interface GigabitEthernet0/0
   ip address 192.168.1.1 255.255.255.0
   no shutdown
   exit
   ip route 0.0.0.0 0.0.0.0 192.168.1.254
   exit
   write memory