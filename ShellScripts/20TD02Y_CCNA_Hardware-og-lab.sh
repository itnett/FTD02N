shell
! Konfigurer VLAN 40 (Management)
vlan database
vlan 40 name Management
exit

! Konfigurer porter til VLAN 40
interface range fastEthernet 0/1 - 24
switchport mode access
switchport access vlan 40
exit