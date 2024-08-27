python
   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("ttk Styling")

   style = ttk.Style()
   style.configure("TButton", font=("Helvetica", 16), foreground="blue")

   tk.Label(root, text="Trykk på knappen:").pack(pady=10)
   ttk.Button(root, text="Knapp").pack(pady=10)

   root.mainloop()