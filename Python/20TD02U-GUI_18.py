python
import tkinter as tk

root = tk.Tk()
root.title("Event Handling")

def on_key(event):
    tk.messagebox.showinfo("Tastetrykk", f"Du trykket: {event.keysym}")

def on_click(event):
    tk.messagebox.showinfo("Musesklikk", f"Du klikket på posisjon: {event.x}, {event.y}")

root.bind("<Key>", on_key)
root.bind("<Button-1>", on_click)

tk.Label(root, text="Trykk en tast eller klikk med musen").pack(pady=20)

root.mainloop()