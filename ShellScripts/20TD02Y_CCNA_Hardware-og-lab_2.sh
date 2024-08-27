shell
configure terminal
vlan 10
name LAN
exit
interface range fastEthernet 0/1 - 24
switchport mode access
switchport access vlan 10
exit