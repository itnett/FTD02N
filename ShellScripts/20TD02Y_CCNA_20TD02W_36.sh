shell
   configure terminal
   crypto isakmp policy 1
   authentication pre-share
   encryption aes
   hash sha
   group 2
   lifetime 86400
   exit

   crypto isakmp key VPN_KEY address 0.0.0.0

   crypto ipsec transform-set TRANSFORM_SET esp-aes esp-sha-hmac

   crypto map VPN_MAP 10 ipsec-isakmp
   set peer 198.51.100.1
   set transform-set TRANSFORM_SET
   match address 101
   exit

   interface GigabitEthernet1/0/1
   crypto map VPN_MAP
   exit