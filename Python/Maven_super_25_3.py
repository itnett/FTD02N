python
import tkinter as tk

# Funksjon for å legge til en oppgave i listen
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

# Funksjon for å fjerne den valgte oppgaven
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

# Oppsett av hovedvinduet
window = tk.Tk()
window.title("Oppgaveliste")

# Inndatafelt og knapp for å legge til oppgaver
frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=50)
entry_task.pack()

button_add_task = tk.Button(window, text="Legg til oppgave", command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(window, text="Fjern valgt oppgave", command=delete_task)
button_delete_task.pack()

# Starter Tkinter-eventloopen
window.mainloop()