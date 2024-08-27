python
import tkinter as tk
from tkinter import simpledialog

def ask_name():
    name = simpledialog.askstring("Input", "Hva er ditt navn?")
    if name:
        tk.messagebox.showinfo("Name", f"Hei, {name}!")

root = tk.Tk()
tk.Button(root, text="Be om navn", command=ask_name).pack(pady=20)
root.mainloop()