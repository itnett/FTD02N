shell
vlan 30
name Guest_Network
exit
vlan 40
name Management
exit

interface vlan 30
ip address 192.168.30.1/24
exit
interface vlan 40
ip address 192.168.40.1/24
exit

interface ethernet 1/1
switchport mode trunk
switchport trunk allowed vlan 30,40
exit

feature hsrp
interface vlan 30
hsrp 1
ip 192.168.30.254
exit

interface vlan 40
hsrp 1
ip 192.168.40.254
exit