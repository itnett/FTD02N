python
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Min Applikasjon")

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill="both")

        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)

        notebook.add(frame1, text="Data")
        notebook.add(frame2, text="Graf")

        # Data Frame
        data = {'Navn': ['Ola', 'Kari', 'Per'],
                'Alder': [23, 25, 21]}
        df = pd.DataFrame(data)

        tree = ttk.Treeview(frame1, columns=("Navn", "Alder"), show='headings')
        tree.heading("Navn", text="Navn")
        tree.heading("Alder", text="Alder")
        tree.pack(expand=True, fill="both")

        for index, row in df.iterrows():
            tree.insert("", tk.END, values=(row["Navn"], row["Alder"]))

        # Graf
        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.plot(df["Navn"], df["Alder"])

        canvas = FigureCanvasTkAgg(fig, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def create_menu(self):
        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Åpne", command=self.dummy_action)
        filemenu.add_command(label="Lagre", command=self.dummy_action)
        filemenu.add_separator()
        filemenu.add_command(label="Avslutt", command=self.root.quit)
        menubar.add_cascade(label="Fil", menu=filemenu)

        self.root.config(menu=menubar)

    def dummy_action(self):
        messagebox.showinfo("Info", "Denne

 funksjonen er ikke implementert ennå")

root = tk.Tk()
app = MyApp(root)
root.mainloop()