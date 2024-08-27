python
   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("Progressbar Eksempel")

   tk.Label(root, text="Fremdrift:").pack(pady=10)

   progressbar = ttk.Progressbar(root, length=200, mode="determinate")
   progressbar.pack(pady=10)

   def start_progress():
       progressbar['value'] = 0
       root.update_idletasks()
       for i in range(100):
           progressbar['value'] += 1
           root.update_idletasks()
           root.after(50)

   tk.Button(root, text="Start", command=start_progress).pack(pady=10)

   root.mainloop()