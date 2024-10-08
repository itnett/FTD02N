python
   import tkinter as tk
   from tkinter import ttk

   root = tk.Tk()
   root.title("Treeview Eksempel")

   tree = ttk.Treeview(root)
   tree.pack(pady=10)

   tree.insert("", "end", "root1", text="Root 1")
   tree.insert("", "end", "root2", text="Root 2")

   tree.insert("root1", "end", "child1", text="Child 1")
   tree.insert("root1", "end", "child2", text="Child 2")
   tree.insert("root2", "end", "child3", text="Child 3")

   root.mainloop()