shell
   configure terminal
   interface vlan 1
   ip address 192.168.1.2 255.255.255.0
   exit
   interface gigabitEthernet 1/0/1
   switchport mode access
   switchport access vlan 1
   exit