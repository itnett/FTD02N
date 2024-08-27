shell
    configure terminal
    vlan 10
    name IoT_Sensors
    exit
    vlan 20
    name IoT_Actuators
    exit

    interface range gigabitEthernet 1/0/1 - 12
    switchport mode access
    switchport access vlan 10
    exit

    interface range gigabitEthernet 1/0/13 - 24
    switchport mode access
    switchport access vlan 20
    exit

    interface gigabitEthernet 1/0/25
    switchport mode trunk
    switchport trunk allowed vlan 10,20
    exit