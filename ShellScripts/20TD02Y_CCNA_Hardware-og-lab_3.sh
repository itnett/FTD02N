shell
configure terminal
vlan 20
name DMZ
vlan 30
name Guest_Network
exit
interface range gigabitEthernet 0/1 - 24
switchport mode access
switchport access vlan 20
exit
interface gigabitEthernet 0/25
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
exit