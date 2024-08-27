python
# Definerer en funksjon for å sende e-post
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Oppretter en forbindelse til Gmail SMTP-server
        server.ehlo()  # Initierer forbindelsen
        server.starttls()  # Krypterer forbindelsen ved hjelp av TLS
        server.login('gammusicrew@gmail.com', '**********')  # Logger inn på senderens e-postkonto
        server.sendmail('madhavampire@gmail.com', to, content)  # Sender e-post
        server.close()  # Lukker forbindelsen
        speak("Email has been sent!")
    except Exception as e:
        speak("Mail not sent due to some error!")
        print(f"Error: {e}")