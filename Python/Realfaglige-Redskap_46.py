python
import tkinter as tk

def button_click():
    label.config(text="Knappen ble trykket!")

window = tk.Tk()
label = tk.Label(text="Hei, Tkinter!")
button = tk.Button(text="Trykk her", command=button_click)
label.pack()
button.pack()
window.mainloop()