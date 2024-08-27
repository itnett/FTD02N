bash
    hping3 -S $TARGET -p $open_ports -c 1
    hping3 -F $TARGET -p $open_ports -c 1
    hping3 -UPF $TARGET -p $open_ports -c 1