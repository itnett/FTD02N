python
import tkinter as tk
from tkinter import messagebox

# Opprett hovedvinduet
root = tk.Tk()
root.title("Avansert GUI")

# Lag et rutenettlayout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Lag en etikett og en inndatafelt
tk.Label(root, text="Skriv noe:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Lag en funksjon som viser en melding
def show_message():
    text = entry.get()
    messagebox.showinfo("Melding", f"Du skrev: {text}")

# Lag en knapp som kaller funksjonen
button = tk.Button(root, text="Vis melding", command=show_message)
button.grid(row=1, column=0, columnspan=2, pady=10)

# Legg til en listeboks med rullefelt
listbox = tk.Listbox(root)
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
scrollbar.grid(row=2, column=2, sticky="ns")
listbox.config(yscrollcommand=scrollbar.set)

# Legg til noen elementer i listeboksen
for i in range(20):
    listbox.insert(tk.END, f"Element {i+1}")

# Lag en meny
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Åpne", command=lambda: messagebox.showinfo("Åpne", "Åpne fil"))
filemenu.add_command(label="Lagre", command=lambda: messagebox.showinfo("Lagre", "Lagre fil"))
filemenu.add_separator()
filemenu.add_command(label="Avslutt", command=root.quit)
menubar.add_cascade(label="Fil", menu=filemenu)

# Legg til menyen i hovedvinduet
root.config(menu=menubar)

# Kjør hovedløkken
root.mainloop()