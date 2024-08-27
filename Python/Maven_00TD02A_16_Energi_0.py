python
import matplotlib.pyplot as plt

# Arbeid, effekt og virkningsgrad
force = 50  # Newton
distance = 10  # meter
time = 5  # sekunder
work = force * distance
power = work / time
efficiency = (work / (work + 10)) * 100  # Anta litt tap

# Visualisere
data = [work, power, efficiency]
labels = ['Arbeid (J)', 'Effekt (W)', 'Virkningsgrad (%)']

plt.bar(labels, data, color=['blue', 'green', 'orange'])
plt.title("Arbeid, Effekt og Virkningsgrad")
plt.show()