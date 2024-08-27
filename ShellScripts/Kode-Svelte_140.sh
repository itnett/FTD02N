bash
   configure terminal
   access-list 1 permit 192.168.1.0 0.0.0.255
   ip nat inside source list 1 interface GigabitEthernet0/0 overload
   interface GigabitEthernet0/0
   ip nat inside
   interface GigabitEthernet0/1
   ip nat outside
   exit
   write memory