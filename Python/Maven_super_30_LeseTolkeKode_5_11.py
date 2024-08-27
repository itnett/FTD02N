python
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = Command()
                to =

 "madhavampire@gmail.com"    
                sendEmail(to, content)
                print("Sent!!!")
            except Exception:
                speak("Mail not sent due to some error!")