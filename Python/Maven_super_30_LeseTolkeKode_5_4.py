python
# Definerer en funksjon for å ønske brukeren velkommen basert på tidspunktet på dagen
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   
    else:
        speak("Good Evening sir!")  
    speak("How can the Moon help you?")