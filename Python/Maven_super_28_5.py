python
import tkinter as tk

def på_tastetrykk(event):
    etikett.config(text=f"Tastetrykk: {event.keysym}")

vindu = tk.Tk()
vindu.title("Hendelsesstyrt Programmering")

etikett = tk.Label(vindu, text="Trykk en tast", font=("Arial", 16))
etikett.pack()

# Binder tastetrykk-hendelsen til funksjonen på_tastetrykk
vindu.bind("<KeyPress>", på_tastetrykk)

vindu.mainloop()