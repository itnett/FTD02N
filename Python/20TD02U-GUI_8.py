python
   import tkinter as tk

   root = tk.Tk()
   root.title("Pack Layout")

   tk.Label(root, text="Top").pack(side=tk.TOP, fill=tk.X)
   tk.Label(root, text="Bottom").pack(side=tk.BOTTOM, fill=tk.X)
   tk.Label(root, text="Left").pack(side=tk.LEFT, fill=tk.Y)
   tk.Label(root, text="Right").pack(side=tk.RIGHT, fill=tk.Y)

   root.mainloop()