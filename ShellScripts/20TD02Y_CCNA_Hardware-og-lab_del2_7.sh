shell
vlan 10
name LAN
exit
vlan 20
name DMZ
exit

interface range gigabitEthernet 0/1 - 24
switchport mode access
switchport access vlan 10
exit

interface gigabitEthernet 0/25
switchport mode trunk
switchport trunk allowed vlan 10,20
exit

ip access-list standard NO_DHCP
deny any
exit

ip dhcp snooping
ip dhcp snooping vlan 10,20
interface range gigabitEthernet 0/1 - 24
ip dhcp snooping trust
exit