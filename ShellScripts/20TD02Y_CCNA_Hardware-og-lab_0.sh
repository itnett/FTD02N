shell
   configure terminal
   vlan 10
   name LAN
   exit
   vlan 20
   name DMZ
   exit
   interface range gigabitEthernet 1/0/1 - 1/0/2
   switchport mode trunk
   switchport trunk allowed vlan 10,20
   exit