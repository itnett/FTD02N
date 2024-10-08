shell
   # På Catalyst 2950
   configure terminal
   vlan 10
   name VLAN10
   exit
   vlan 20
   name VLAN20
   exit
   interface range fastEthernet 0/1 - 12
   switchport mode access
   switchport access vlan 10
   exit
   interface range fastEthernet 0/13 - 24
   switchport mode access
   switchport access vlan 20
   exit

   # På Catalyst 2960G
   configure terminal
   vlan 10
   name VLAN10
   exit
   vlan 20
   name VLAN20
   exit
   interface range gigabitEthernet 0/1 - 12
   switchport mode access
   switchport access vlan 10
   exit
   interface range gigabitEthernet 0/13 - 24
   switchport mode access
   switchport access vlan 20
   exit
   interface gigabitEthernet 0/25
   switchport mode trunk
   exit