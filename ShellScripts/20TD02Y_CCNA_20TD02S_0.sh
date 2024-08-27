shell
   # På Catalyst 3750G
   configure terminal
   vlan 10
   name VLAN10
   exit
   vlan 20
   name VLAN20
   exit
   interface range gigabitEthernet 1/0/1 - 12
   switchport mode access
   switchport access vlan 10
   exit
   interface range gigabitEthernet 1/0/13 - 24
   switchport mode access
   switchport access vlan 20
   exit