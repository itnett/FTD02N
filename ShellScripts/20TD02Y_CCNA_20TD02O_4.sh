shell
# På Catalyst 2960G
interface gigabitEthernet 0/1
switchport mode access
switchport port-security
switchport port-security maximum 2
switchport port-security violation restrict
switchport port-security mac-address sticky
exit