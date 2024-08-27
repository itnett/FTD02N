python
import matplotlib.pyplot as plt

kategorier = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
antall_hendelser = [15, 20, 12, 8, 25]

plt.bar(kategorier, antall_hendelser, color="skyblue")
plt.title("Sikkerhetshendelser per ukedag")
plt.xlabel("Ukedag")
plt.ylabel("Antall hendelser")
plt.show()