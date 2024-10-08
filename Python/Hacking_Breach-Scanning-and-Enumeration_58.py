python
   from flask import Flask, request, render_template
   import subprocess
   import os
   import datetime

   app = Flask(__name__)

   def run_command(command):
       process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       stdout, stderr = process.communicate()
       return stdout.decode(), stderr.decode()

   def perform_scan(target_ip):
       timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
       report_dir = f"reports/{target_ip}_{timestamp}"
       os.makedirs(report_dir, exist_ok=True)

       # Skanninger som før
       # ...

       return report_dir

   def generate_documentation(report_dir, target_ip):
       # Generer dokumentasjon som før
       # ...

   @app.route('/')
   def index():
       return render_template('index.html')

   @app.route('/scan', methods=['POST'])
   def scan():
       target_ip = request.form['target_ip']
       report_dir = perform_scan(target_ip)
       generate_documentation(report_dir, target_ip)
       # Send notification
       send_email_notification(report_dir, target_ip)
       send_webhook_notification(report_dir, target_ip)
       return f"Scan completed. Report saved in {report_dir}/report.txt"

   if __name__ == '__main__':
       app.run(debug=True)