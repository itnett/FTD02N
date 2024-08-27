shell
vlan 10
name LAN
exit
vlan 20
name DMZ
exit

interface vlan 10
ip address 192.168.10.1 255.255.255.0
exit
interface vlan 20
ip address 192.168.20.1 255.255.255.0
exit

interface range gigabitEthernet 1/0/1 - 1/0/24
switchport mode access
switchport access vlan 10
exit

interface gigabitEthernet 1/0/25
switchport mode trunk
switchport trunk allowed vlan 10,20
exit

interface gigabitEthernet 1/0/2
switchport mode trunk
switchport trunk allowed vlan 10,20
exit

ip routing