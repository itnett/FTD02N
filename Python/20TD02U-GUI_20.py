python
   import tkinter as tk
   from tkinter import ttk
   from matplotlib.figure import Figure
   from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

   root = tk.Tk()
   root.title("Integrasjon med Matplotlib")

   fig = Figure(figsize=(5, 4), dpi=100)
   plot = fig.add_subplot(1, 1, 1)
   plot.plot([0.5, 1.5, 2.5], [10, 20, 30])

   canvas = FigureCanvasTkAgg(fig, master=root)
   canvas.draw()
   canvas.get_tk_widget().pack(pady=20)

   root.mainloop()