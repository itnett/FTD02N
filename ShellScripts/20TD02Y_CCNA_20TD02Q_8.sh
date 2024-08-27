shell
   configure terminal
   access-list 101 permit tcp any any eq 22
   access-list 101 deny ip any any
   interface gigabitEthernet 0/1
   ip access-group 101 in
   exit