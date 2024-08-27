shell
vlan 50
name Servers
exit

interface range gigabitEthernet 1/0/1 - 1/0/24
switchport mode access
switchport access

 vlan 50
exit

interface gigabitEthernet 1/0/25
switchport mode trunk
switchport trunk allowed vlan 50
exit

interface vlan 50
ip address 192.168.50.1 255.255.255.0
exit

ip routing