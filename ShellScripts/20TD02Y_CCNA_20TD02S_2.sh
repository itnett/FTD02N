shell
   access-list 101 deny ip any any
   interface gigabitEthernet 0/1
   ip access-group 101 in
   exit