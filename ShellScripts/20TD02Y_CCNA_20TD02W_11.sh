shell
   configure terminal
   access-list 100 deny ip 192.168.1.0 0.0.0.255 any
   access-list 100 permit ip any any
   interface GigabitEthernet0/0
   ip access-group 100 in
   exit