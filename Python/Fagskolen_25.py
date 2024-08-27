python
import tkinter as tk
from tkinter import ttk, messagebox
from database import create_connection
from models import Vare

def prompt_for_credentials():
    dialog = tk.Tk()
    dialog.title("Database innlogging")
    dialog.geometry("300x200")
    # Fields for user inputs...
    def on_ok():
        global db_user, db_password, db_host, db_name, db_port
        # Fetch values from the entries...
        dialog.destroy()
    tk.Button(dialog, text="Ok", command=on_ok).pack()
    tk.Button(dialog, text="Avbryt", command=dialog.destroy).pack()
    dialog.mainloop()

def list_varelager(connection):
    cursor = connection.cursor()
    cursor.callproc('VisVarelager')
    varer = []
    for result in cursor.stored_results():
        for row in result.fetchall():
            varer.append(Vare(*row))
    return varer

def update_output_varelager():
    data = list_varelager(conn)
    output_field.delete('1.0', tk.END)
    for item in data:
        output_field.insert(tk.END, str(item) + "\n")

# Additional functions for other database operations...

if __name__ == "__main__":
    prompt_for_credentials()
    conn = create_connection(db_user, db_password, db_host, db_name, db_port)
    if conn:
        root = tk.Tk()
        # GUI setup and mainloop...