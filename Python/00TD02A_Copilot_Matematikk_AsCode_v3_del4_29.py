python
import tkinter as tk

def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name}")

app = tk.Tk()
app.title("Greeting App")

name_label = tk.Label(app, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

greet_button = tk.Button(app, text="Greet", command=greet)
greet_button.pack()

greeting_label = tk.Label(app, text="")
greeting_label.pack()

app.mainloop()