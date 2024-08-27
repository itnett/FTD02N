bash
    alert icmp any any -> any any (msg:"ICMP echo request detected"; itype:8; sid:1000001; rev:1;)