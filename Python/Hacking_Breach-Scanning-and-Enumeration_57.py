python
   import requests

   def send_webhook_notification(report_dir, target_ip):
       webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
       message = {
           "text": f"Scan completed. Report saved in {report_dir}/report.txt for {target_ip}"
       }
       requests.post(webhook_url, json=message)