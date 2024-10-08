shell
   configure terminal
   feature vpc
   vpc domain 1
   role priority 100
   peer-keepalive destination 192.168.1.2 source 192.168.1.1
   interface port-channel 1
   vpc peer-link
   interface ethernet 1/1
   channel-group 1 mode active
   exit