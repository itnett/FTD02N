python
import smtplib
import imaplib
import email
from email.mime.text import MIMEText

# SMTP-server konfigurasjon
smtp_server = 'smtp.yourdomain.com'
smtp_port = 587
smtp_user = 'your-email@yourdomain.com'
smtp_password = 'your-email-password'

# IMAP-server konfigurasjon
imap_server = 'imap.yourdomain.com'
imap_user = 'your-email@yourdomain.com'
imap_password = 'your-email-password'

# Ikke-eksisterende adresse på måldomenet
target_email = 'nonexistant@example.com'

# E-postinnhold
msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = smtp_user
msg['To'] = target_email

# Send e-post
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, [target_email], msg.as_string())

# Vent noen minutter for å motta NDR-meldingen

# Koble til IMAP-server for å lese NDR-meldingen
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(imap_user, imap_password)
mail.select('inbox')

# Søk etter NDR-meldinger
status, response = mail.search(None, 'FROM', '"Mail Delivery Subsystem"')

# Hent og skriv ut NDR-meldinger
if status == 'OK':
    for num in response[0].split():
        status, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        print(email_message)

mail.logout()