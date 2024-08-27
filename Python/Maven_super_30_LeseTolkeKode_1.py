python
# Importerer nødvendige biblioteker og moduler for å starte
import tkinter as tk  # GUI-biblioteket Tkinter
import requests  # For API-kall
import json  # For håndtering av JSON-data
import os  # For filbehandling
import hashlib  # For datasikkerhet, her brukt til hashing
from tkinter import messagebox  # For meldingsbokser i GUI

# Starten på et objektorientert program: Definerer en klasse for Notatverktøyet
class NotatVerktøy:
    def __init__(self, root):
        """Konstruktørmetoden for å initialisere GUI-komponenter og variabler"""
        self.root = root  # Rotvinduet for applikasjonen
        self.root.title("Notatverktøy")  # Setter tittelen på hovedvinduet

        # Variabeldeklarasjoner
        self.filnavn = "notater.txt"  # Filen hvor notater lagres
        self.nåværende_notat = ""  # Holder innholdet av det nåværende notatet

        # GUI-komponenter
        self.text_area = tk.Text(self.root, wrap='word')  # Tekstområde for å skrive notater
        self.text_area.pack(expand=True, fill='both')  # Plasserer tekstområdet i hovedvinduet

        # Menylinje
        self.menylinje = tk.Menu(self.root)  # Lager en menylinje
        self.root.config(menu=self.menylinje)  # Setter menylinjen i hovedvinduet

        # Filer-menyen
        fil_meny = tk.Menu(self.menylinje, tearoff=0)  # Lager en undermeny for filer
        self.menylinje.add_cascade(label="Filer", menu=fil_meny)  # Legger til "Filer" i menylinjen
        fil_meny.add_command(label="Lagre", command=self.lagre_notat)  # Legger til "Lagre"-kommando
        fil_meny.add_command(label="Åpne", command=self.åpne_notat)  # Legger til "Åpne"-kommando

        # Hjelp-menyen
        hjelp_meny = tk.Menu(self.menylinje, tearoff=0)  # Lager en undermeny for hjelp
        self.menylinje.add_cascade(label="Hjelp", menu=hjelp_meny)  # Legger til "Hjelp" i menylinjen
        hjelp_meny.add_command(label="Om", command=self.om)  # Legger til "Om"-kommando

        # Laster tidligere notater om de finnes
        self.åpne_notat()

    def lagre_notat(self):
        """Lagrer det nåværende notatet til en fil"""
        try:
            with open(self.filnavn, 'w') as fil:  # Åpner filen i skrivemodus
                filinnhold = self.text_area.get(1.0, tk.END)  # Henter tekst fra tekstområdet
                fil.write(filinnhold)  # Skriver teksten til filen
            messagebox.showinfo("Lagre", "Notat lagret!")  # Viser en suksessmelding
        except IOError as e:  # Fanger opp fil I/O-feil
            messagebox.showerror("Feil", f"Kunne ikke lagre notatet: {e}")

    def åpne_notat(self):
        """Åpner et notat fra fil hvis det eksisterer"""
        if os.path.exists(self.filnavn):  # Sjekker om filen eksisterer
            try:
                with open(self.filnavn, 'r') as fil:  # Åpner filen i lesemodus
                    innhold = fil.read()  # Leser filinnholdet
                    self.text_area.delete(1.0, tk.END)  # Tømmer tekstområdet
                    self.text_area.insert(tk.END, innhold)  # Setter inn filinnholdet
            except IOError as e:  # Fanger opp fil I/O-feil
                messagebox.showerror("Feil", f"Kunne ikke åpne notatet: {e}")

    def om(self):
        """Viser en informasjonstekst om applikasjonen"""
        messagebox.showinfo("Om", "Notatverktøy v1.0 - Et enkelt notatverktøy")

    def krypter_innhold(self, innhold):
        """Krypterer innholdet ved hjelp av en hashfunksjon"""
        hasher = hashlib.sha256()  # Bruker SHA-256 hashing algoritmen
        hasher.update(innhold.encode('utf-8'))  # Oppdaterer hash med innholdet
        return hasher.hexdigest()  # Returnerer den heksadesimale representasjonen

    def hent_data_fra_api(self):
        """Eksempel på å hente data fra et API (f.eks. OpenWeatherMap)"""
        api_url = "https://api.openweathermap.org/data/2.5/weather?q=Oslo&appid=ditt_api_nøkkel"
        try:
            respons = requests.get(api_url)  # Sender en GET-forespørsel til API-en
            data = respons.json()  # Konverterer svaret til JSON
            temperatur = data['main']['temp']  # Henter temperaturen fra dataen
            return f"Temperaturen i Oslo er {temperatur - 273.15:.2f}°C"
        except requests.RequestException as e:  # Fanger opp nettverksfeil
            messagebox.showerror("Feil", f"Kunne ikke hente data fra API: {e}")
            return "Ingen data tilgjengelig"

# Lager rotvinduet og kjører applikasjonen
if __name__ == "__main__":
    root = tk.Tk()  # Oppretter hovedvinduet
    app = NotatVerktøy(root)  # Instansierer klassen
    root.mainloop()  # Starter hovedløkken for GUI-en