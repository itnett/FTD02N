shell
   configure terminal
   interface GigabitEthernet0/0
   ipv6 address 2001:db8:1::1/64
   no shutdown
   exit
   ipv6 unicast-routing