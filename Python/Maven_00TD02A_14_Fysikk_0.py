python
import matplotlib.pyplot as plt

# SI-enheter og prefikser
units = ["m", "km", "cm", "mm"]
values = [1, 0.001, 100, 1000]  # 1 meter, 0.001 kilometer, 100 centimeter, 1000 millimeter

plt.bar(units, values, color='blue')
plt.title("Konvertering mellom SI-enheter for lengde")
plt.xlabel("Enheter")
plt.ylabel("Verdier i forhold til 1 meter")
plt.show()