shell
configure terminal
vlan 40
name Management
exit
interface range fastEthernet 0/1 - 24
switchport mode access
switchport access vlan 40
exit