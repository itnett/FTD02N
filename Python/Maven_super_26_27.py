python
import tkinter as tk

def legg_til_oppgave():
    oppgave = oppgave_inn.get()
    if oppgave:
        oppgaveliste.insert(tk.END, oppgave)
        oppgave_inn.delete(0, tk.END)

# Hovedvinduet
vindu = tk.Tk()
vindu.title("Oppgaveliste")

# Tekstboks for å legge inn oppgaver
oppgave_inn = tk.Entry(vindu, width=50)
oppgave_inn.pack(pady=10)

# Legg til-knapp
legg_til_knapp = tk.Button(vindu, text="Legg til oppgave", command=legg_til_oppgave)
legg_til_knapp.pack(pady=10)

# Listeboks for å vise oppgaver
oppgaveliste = tk.Listbox(vindu, width=50, height=10)
oppgaveliste.pack(pady=10)

# Kjøre hovedløkken
vindu.mainloop()