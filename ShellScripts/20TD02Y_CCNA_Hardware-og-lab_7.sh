shell
! Konfigurer VLAN 10 (LAN)
vlan database
vlan 10 name LAN
exit

! Konfigurer porter til VLAN 10
interface range fastEthernet 0/1 - 24
switchport mode access
switchport access vlan 10
exit

! Trunk port til 3750G
interface fastEthernet 0/25
switchport mode trunk
switchport trunk allowed vlan 10,20,30,40
exit