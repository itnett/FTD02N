python
   def on_button_click():
       label.config(text="Knappen ble trykket!")

   button = tk.Button(root, text="Trykk meg", command=on_button_click)
   button.pack()