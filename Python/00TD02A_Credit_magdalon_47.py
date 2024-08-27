python
import matplotlib.pyplot as plt

data = [30, 25, 20, 15, 10]
labels = ["Phishing", "Malware", "DoS-angrep", "SQL-injeksjon", "Andre"]

plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("Fordeling av sikkerhetshendelser")
plt.axis("equal")  # Sørger for at diagrammet er en sirkel
plt.show()