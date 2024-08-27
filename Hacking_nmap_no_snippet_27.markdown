# 🌐 Nettverksskanningsteknikker Mindmap

## 🛠️ Nmap Skanningsteknikker
- ### 🔎 Portskanning
  - **TCP Connect Scan** (full åpen)
    - `nmap -sT <target>`
  - **SYN Scan** (halvåpen)
    - `nmap -sS <target>`
  - **FIN Scan**
    - `nmap -sF <target>`
  - **Xmas Scan**
    - `nmap -sX <target>`
  - **Null Scan**
    - `nmap -sN <target>`
  - **UDP Scan**
    - `nmap -sU <target>`
  - **TCP ACK Scan**
    - `nmap -sA <target>`
  - **Window Scan**
    - `nmap -sW <target>`
  - **Maimon Scan**
    - `nmap -sM <target>`
  - **SCTP INIT Scan**
    - `nmap -sY <target>`
  - **SCTP COOKIE-ECHO Scan**
    - `nmap -sZ <target>`

- ### 🔄 OS Fingerprinting
  - **TCP/IP Fingerprinting**
    - `nmap -O <target>`

- ### 🔍 Service Discovery
  - **Service Version Detection**
    - `nmap -sV <target>`

- ### 🕒 Tidsbaserte Skanninger
  - **Idle Scan**
    - `nmap -sI <zombie_host> <target>`
  - **Timing Templates**
    - `nmap -T0 - T5 <target>`

- ### 🚀 Bypass Firewall/IDS Techniques
  - **Fragmented Packets**
    - `nmap -f <target>`
  - **Decoy Scan**
    - `nmap -D RND:10 <target>`
  - **Spoofed Source IP**
    - `nmap -S <spoofed_ip> <target>`

## 🔧 Andre Verktøy
- ### ⚙️ Hping
  - **Hping TCP Syn Scan**
    - `hping3 -S <target> -p <port>`
  - **Hping FIN Scan**
    - `hping3 -F <target> -p <port>`
  - **Hping Xmas Scan**
    - `hping3 -UPF <target> -p <port>`

- ### 🛠️ Masscan
  - **Masscan Full Scan**
    - `masscan -p0-65535 <target> --rate=<rate>`

- ### 🔧 Netcat
  - **Netcat Port Scan**
    - `nc -zv <target> <start_port>-<end_port>`

## 📊 Tolkning av Resultater
- ### 📗 Åpen Port
  - Mottar forventet respons eller SYN-ACK.
- ### 📕 Lukket Port
  - Mottar RST-pakke.
- ### 📙 Filtrert Port
  - Ingen svar eller mottar ICMP unreachable melding.

## 📚 Referanser
- [Nmap Documentation](https://nmap.org/docs.html)
- [Hping3 Documentation](http://www.hping.org/documentation.html)
- [Masscan Documentation](https://github.com/robertdavidgraham/masscan)
- [Netcat Documentation](http://nc110.sourceforge.net/)