python
# Definerer en funksjon for å lytte til brukerens kommandoer
def Command():
    r = sr.Recognizer()  # Initialiserer talegjenkjenningsmotoren
    with sr.Microphone() as source:  # Bruker mikrofonen som lydkilde
        print("Listening...")
        r.pause_threshold = 1  # Setter pause terskelen før gjenkjennelse starter
        audio = r.listen(source)  # Lytter til lyd og lagrer den som variabelen 'audio'
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')  # Bruker Google's talegjenkjenning for å konvertere lyd til tekst
        print(f"You said: {query}\n")  # Skriver ut hva brukeren sa
    except Exception:
        print("Say that again please...") 
        return None  # Returnerer None hvis det er en feil
    return query.lower()  # Returnerer brukerens kommando i små bokstaver