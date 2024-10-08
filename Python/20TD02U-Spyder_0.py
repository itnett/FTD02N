python
import os
import json
import requests
import tkinter as tk
from tkinter import messagebox
from matplotlib import pyplot as plt
from hashlib import sha256

# --- PROGRAMSTRUKTURER OG DATASTRUKTURER ---
def basic_program_structure():
    """Enkel funksjon for å demonstrere variabeldeklarasjoner, løkker og kontrollstrukturer."""
    print("Grunnleggende programstruktur")
    x = 10
    y = 20
    sum = x + y
    print(f"Sum: {sum}")
    
    for i in range(5):
        print(f"Løkke iterasjon: {i}")
        
    if sum > 15:
        print("Sum er større enn 15")

basic_program_structure()

# --- BIBLIOTEKER OG FILBEHANDLING ---
def file_handling_example():
    """Demonstrerer grunnleggende filbehandling i Python."""
    with open('example.txt', 'w') as file:
        file.write("Dette er en testfil.\n")
        file.write("Filbehandling i Python er enkelt.\n")
    
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Innholdet i filen:")
        print(content)

file_handling_example()

# --- FUNKSJONER OG METODER ---
def add_numbers(a, b):
    """Legger til to tall."""
    return a + b

print(f"Resultat av add_numbers: {add_numbers(3, 4)}")

# --- OBJEKTORIENTERT PROGRAMMERING ---
class Person:
    """En enkel klasse for å representere en person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hei, jeg heter {self.name} og er {self.age} år gammel."

p = Person("Alice", 30)
print(p.greet())

# --- DEBUGGING, TESTING OG UNNTAKSBEHANDLING ---
def divide(a, b):
    """Dividerer to tall med unntaksbehandling for å håndtere null-divisjon."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Feil: Kan ikke dele med null.")
        return None

print(f"Resultat av divide: {divide(10, 2)}")
print(f"Resultat av divide med null-divisjon: {divide(10, 0)}")

# --- API EKSEMPEL ---
def fetch_weather(city):
    """Henter værdata fra en offentlig API."""
    api_key = "din_api_nøkkel"  # Sett inn din API-nøkkel her
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print(f"Været i {city}: {data['weather'][0]['description']}")
    else:
        print(f"Feil ved henting av værdata for {city}")

# fetch_weather("Oslo")  # Aktiver denne linjen ved å sette inn en gyldig API-nøkkel

# --- GUI EKSEMPEL ---
def gui_example():
    """Oppretter et enkelt GUI ved bruk av Tkinter."""
    def on_button_click():
        name = entry.get()
        messagebox.showinfo("Hei", f"Hei, {name}!")
    
    root = tk.Tk()
    root.title("GUI Eksempel")
    
    label = tk.Label(root, text="Skriv inn navnet ditt:")
    label.pack()
    
    entry = tk.Entry(root)
    entry.pack()
    
    button = tk.Button(root, text="Klikk meg", command=on_button_click)
    button.pack()
    
    root.mainloop()

gui_example()

# --- UML EKSEMPEL ---
# UML-diagrammer kan lages ved hjelp av ulike verktøy, som UMLet, Lucidchart eller lignende.
# Eksempel på hvordan en UML-klasse for Person-klassen kan se ut:
# 
# +-----------------+
# |     Person      |
# +-----------------+
# | - name: str     |
# | - age: int      |
# +-----------------+
# | + greet() -> str|
# +-----------------+

# --- DATASIKKERHET ---
def encrypt_data(data):
    """Krypterer data ved bruk av SHA-256 hashing."""
    return sha256(data.encode()).hexdigest()

sensitive_data = "dette_er_hemmelig"
encrypted_data = encrypt_data(sensitive_data)
print(f"Kryptert data: {encrypted_data}")

# --- SAMLE FUNKSJONER OG EKSEMPLER ---
def run_all_examples():
    basic_program_structure()
    file_handling_example()
    print(f"Resultat av add_numbers: {add_numbers(5, 7)}")
    p = Person("Bob", 25)
    print(p.greet())
    print(f"Resultat av divide: {divide(20, 4)}")
    print(f"Resultat av divide med null-divisjon: {divide(20, 0)}")
    # fetch_weather("Bergen")  # Aktiver denne linjen ved å sette inn en gyldig API-nøkkel
    gui_example()
    print(f"Kryptert data: {encrypt_data('eksempeldata')}")

run_all_examples()