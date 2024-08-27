python
import tkinter as tk

# Opprett hovedvinduet
root = tk.Tk()
root.title("Mitt første GUI")

# Lag en etikett (label)
label = tk.Label(root, text="Hei, verden!")
label.pack()

# Lag en knapp (button)
def on_button_click():
    label.config(text="Knappen ble trykket!")

button = tk.Button(root, text="Trykk meg", command=on_button_click)
button.pack()

# Kjør hovedløkken
root.mainloop()