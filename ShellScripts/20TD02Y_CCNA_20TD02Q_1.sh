shell
   configure terminal
   interface gigabitEthernet 0/0
   ip address 192.168.1.1 255.255.255.0
   no shutdown
   exit
   interface gigabitEthernet 0/1
   ip address 10.0.0.1 255.255.255.0
   no shutdown
   exit
   ip route 0.0.0.0 0.0.0.0 192.168.1.254