bash
    for port in $(echo $open_ports | tr ',' ' '); do
        nc -vz $TARGET $port
    done