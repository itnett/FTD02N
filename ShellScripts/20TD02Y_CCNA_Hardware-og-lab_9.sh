shell
! Konfigurer VLAN 10, 20, 30 og 40
vlan 10
name LAN
vlan 20
name DMZ
vlan 30
name Guest_Network
vlan 40
name Management
exit

! Konfigurer SVIs (Switch Virtual Interfaces) for routing
interface vlan 10
ip address 192.168.10.1 255.255.255.0
exit
interface vlan 20
ip address 192.168.20.1 255.255.255.0
exit
interface vlan 30
ip address 192.168.30.1 255.255.255.0
exit
interface vlan 40
ip address 192.168.40.1 255.255.255.0
exit

! Trunk port til Nexus 5548UP og 2960G
interface gigabitEthernet 1/0/25
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
exit

! Aktiver IP routing
ip routing