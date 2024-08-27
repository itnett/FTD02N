shell
   configure terminal
   ip access-list extended BLOCK_UNAUTHORIZED
   deny ip 192.168.1.0 0.0.0.255 any
   permit ip any any
   exit
   interface Ethernet1/1
   ip access-group BLOCK_UNAUTHORIZED in
   exit