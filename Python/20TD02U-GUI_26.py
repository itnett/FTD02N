python
import tkinter as tk

translations = {
    "en": {"greet": "Hello, world!", "button": "Click me"},
    "no": {"greet": "Hei, verden!", "button": "Trykk meg"}
}

def change_language(lang):
    greeting.config(text=translations[lang]["greet"])
    button.config(text=translations[lang]["button"])

root = tk.Tk()
root.title("Flerspråklig Grensesnitt")

greeting = tk.Label(root, text=translations["en"]["greet"])
greeting.pack(pady=10)

button = tk.Button(root, text=translations["en"]["button"])
button.pack(pady=10)

tk.Button(root, text="English", command=lambda: change_language("en")).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Norsk", command=lambda: change_language("no")).pack(side=tk.RIGHT, padx=10)

root.mainloop()