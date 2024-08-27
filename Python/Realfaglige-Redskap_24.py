python
import tkinter as tk

def klikk():
    label.config(text="Knappen ble trykket!")

window = tk.Tk()
label = tk.Label(text="Hei, Tkinter!")
knapp = tk.Button(text="Trykk her", command=klikk)
label.pack()
knapp.pack()
window.mainloop()