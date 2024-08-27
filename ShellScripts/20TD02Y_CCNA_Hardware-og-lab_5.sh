shell
configure terminal
vlan 10
name LAN
vlan 20
name DMZ
vlan 30
name Guest_Network
vlan 40
name Management
exit

interface vlan 10
ip address 192.168.10.254/24
exit
interface vlan 20
ip address 192.168.20.254/24
exit
interface vlan 30
ip address 192.168.30.254/24
exit
interface vlan 40
ip address 192.168.40.254/24
exit

interface ethernet 1/1
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
exit

feature vpc
vpc domain 1
role priority 100
peer-keepalive destination 192.168.1.2 source 192.168.1.1
interface port-channel 1
vpc peer-link
interface ethernet 1/1
channel-group 1 mode active
exit