python
import tkinter as tk

def on_button_click():
    print("Knapp klikket")

root = tk.Tk()
root.title("Enkel GUI")

button = tk.Button(root, text="Klikk meg!", command=on_button_click)
button.pack()

root.mainloop()