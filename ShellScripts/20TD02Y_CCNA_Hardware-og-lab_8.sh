shell
! Konfigurer VLAN 20 (DMZ) og VLAN 30 (Guest Network)
vlan 20
name DMZ
vlan 30
name Guest_Network
exit

! Konfigurer porter til VLAN 20
interface range gigabitEthernet 0/1 - 24
switchport mode access
switchport access vlan 20
exit

! Trunk port til 3750G
interface gigabitEthernet 0/25
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
exit