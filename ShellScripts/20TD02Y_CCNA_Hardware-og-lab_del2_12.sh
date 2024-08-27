shell
vlan 50
name Servers
exit

interface vlan 50
ip address 192.168.50.254/24
exit

interface ethernet 1/1
switchport mode trunk
switchport trunk allowed vlan 50
exit