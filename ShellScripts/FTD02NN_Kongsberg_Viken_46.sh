bash
  # Konfigurer en VLAN på en Cisco-svitsj
  enable
  configure terminal
  vlan 10
  name HR_VLAN
  exit
  interface GigabitEthernet0/1
  switchport mode access
  switchport access vlan 10
  exit