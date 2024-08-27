bash
    nmap -sF -p $open_ports $TARGET
    nmap -sX -p $open_ports $TARGET
    nmap -sN -p $open_ports $TARGET