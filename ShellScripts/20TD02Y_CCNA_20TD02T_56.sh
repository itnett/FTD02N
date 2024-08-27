shell
configure terminal
vlan 10
name Database
exit
interface fastEthernet 0/1
switchport mode access
switchport access vlan 10
exit