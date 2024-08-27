shell
vlan 10
name LAN
exit
vlan 20
name DMZ
exit

interface range fastEthernet 0/1 - 24
switchport mode access
switchport access vlan 10
exit

interface fastEthernet 0/25
switchport mode trunk
switchport trunk allowed vlan 10,20
exit