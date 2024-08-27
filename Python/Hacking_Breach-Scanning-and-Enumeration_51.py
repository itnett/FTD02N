python
   import subprocess
   import os
   import datetime
   import cherrypy

   def run_command(command):
       process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stdout, stderr = process.communicate()
       return stdout.decode(), stderr.decode()

   def perform_scan(target_ip):
       timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
       report_dir = f"reports/{target_ip}_{timestamp}"
       os.makedirs(report_dir, exist_ok=True)

       # Nmap scan
       nmap_command = f"nmap -sS -T4 -n -Pn -p- -oN {report_dir}/nmap_all_ports.txt {target_ip}"
       nmap_output, nmap_error = run_command(nmap_command)

       # Detailed Nmap scan
       nmap_detail_command = f"nmap -sC -A -T4 -n -Pn -p80,4444,8443 -oN {report_dir}/nmap_deepscan.txt {target_ip}"
       nmap_detail_output, nmap_detail_error = run_command(nmap_detail_command)

       # Gobuster scan
       gobuster_command = f"gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirb/common.txt -o {report_dir}/gobuster.txt"
       gobuster_output, gobuster_error = run_command(gobuster_command)

       # Nikto scan
       nikto_command = f"nikto -h http://{target_ip} -o {report_dir}/nikto.htm"
       nikto_output, nikto_error = run_command(nikto_command)

       return report_dir

   def generate_documentation(report_dir, target_ip):
       with open(f"{report_dir}/report.txt", 'w') as report:
           report.write(f"Automated Scan Report for {target_ip}\n")
           report.write(f"Scan conducted on: {datetime.datetime.now()}\n\n")

           report.write("Nmap All Ports Scan:\n")
           with open(f"{report_dir}/nmap_all_ports.txt", 'r') as nmap_all:
               report.write(nmap_all.read())
           
           report.write("\n\nNmap Detailed Scan:\n")
           with open(f"{report_dir}/nmap_deepscan.txt", 'r') as nmap_detail:
               report.write(nmap_detail.read())
           
           report.write("\n\nGobuster Scan:\n")
           with open(f"{report_dir}/gobuster.txt", 'r') as gobuster:
               report.write(gobuster.read())
           
           report.write("\n\nNikto Scan:\n")
           with open(f"{report_dir}/nikto.htm", 'r') as nikto:
               report.write(nikto.read())

   class WebServer:
       @cherrypy.expose
       def index(self):
           return """<html>
                       <head><title>Automated Scan</title></head>
                       <body>
                           <h2>Enter Target IP for Automated Scan</h2>
                           <form method="post" action="scan">
                               <input type="text" name="target_ip" />
                               <button type="submit">Start Scan</button>
                           </form>
                       </body>
                   </html>"""

       @cherrypy.expose
       def scan(self, target_ip):
           report_dir = perform_scan(target_ip)
           generate_documentation(report_dir, target_ip)
           return f"Scan completed. Report saved in {report_dir}/report.txt"

   if __name__ == "__main__":
       cherrypy.quickstart(WebServer())