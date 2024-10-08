python
   import smtplib
   from email.mime.text import MIMEText

   def send_email_notification(report_dir, target_ip):
       msg = MIMEText(f"Scan completed. Report saved in {report_dir}/report.txt")
       msg['Subject'] = f"Scan Report for {target_ip}"
       msg['From'] = 'your_email@example.com'
       msg['To'] = 'recipient@example.com'

       with smtplib.SMTP('smtp.example.com') as server:
           server.login('your_email@example.com', 'your_password')
           server.sendmail('your_email@example.com', ['recipient@example.com'], msg.as_string())