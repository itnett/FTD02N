python
import matplotlib.pyplot as plt

# Eksempeldata
måneder = ['Januar', 'Februar', 'Mars', 'April']
salg = [120, 150, 180, 220]

# Lage et søylediagram
plt.bar(måneder, salg)
plt.title('Salg per måned')
plt.xlabel('Måned')
plt.ylabel('Salg')
plt.show()