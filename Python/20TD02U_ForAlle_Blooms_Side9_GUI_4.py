python
def on_button_click():
    print("Knappen ble klikket!")

knapp = tk.Button(vindu, text="Klikk meg", command=on_button_click)
knapp.pack()