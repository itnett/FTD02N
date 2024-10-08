python
import matplotlib.pyplot as plt

systemer = ["System A", "System B", "System C"]
responstid_ms = [50, 80, 65]

plt.bar(systemer, responstid_ms, color=["blue", "orange", "green"], label="Responstid (ms)")
plt.title("Responstid for ulike systemer")
plt.xlabel("System")
plt.ylabel("Responstid (ms)")
plt.legend()
plt.show()