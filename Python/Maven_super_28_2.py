python
import tkinter as tk

def vis_hilsen():
    etikett.config(text="Knappen ble trykket!")

vindu = tk.Tk()
vindu.title("Knapp Eksempel")

etikett = tk.Label(vindu, text="Trykk knappen nedenfor", font=("Arial", 16))
etikett.pack()

# Legge til en knapp
knapp = tk.Button(vindu, text="Trykk meg", command=vis_hilsen)
knapp.pack()

vindu.mainloop()