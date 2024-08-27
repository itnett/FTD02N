python
import matplotlib.pyplot as plt

sårbarheter = {"kritisk": 5, "høy": 10, "middels": 15, "lav": 20}

plt.pie(sårbarheter.values(), labels=sårbarheter.keys(), autopct="%1.1f%%", startangle=140, explode=[0.1, 0, 0, 0])
plt.title("Fordeling av sårbarheter etter alvorlighetsgrad")
plt.axis("equal")
plt.show()