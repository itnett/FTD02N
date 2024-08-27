python
   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("Notebook Eksempel")

   notebook = ttk.Notebook(root)
   notebook.pack(pady=10, expand=True)

   frame1 = ttk.Frame(notebook, width=400, height=280)
   frame2 = ttk.Frame(notebook, width=400, height=280)

   frame1.pack(fill="both", expand=True)
   frame2.pack(fill="both", expand=True)

   notebook.add(frame1, text="Fane 1")
   notebook.add(frame2, text="Fane 2")

   tk.Label(frame1, text="Innhold i Fane 1").pack(pady=20)
   tk.Label(frame2, text="Innhold i Fane 2").pack(pady=20)

   root.mainloop()