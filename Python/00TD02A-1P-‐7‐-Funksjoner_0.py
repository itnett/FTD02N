python
# Trinket-kode for Leksjon 7.1: Koordinatsystemet

import matplotlib.pyplot as plt

# Funksjon for å tegne koordinatsystemet og plotte et punkt
def plot_koordinatsystem(punkt):
    # Opprette figur og akser
    fig, ax = plt.subplots()
    
    # Tegne x-aksen og y-aksen
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    
    # Plot punktet
    ax.plot(punkt[0], punkt[1], 'ro')  # 'ro' betyr rød farge, sirkelpunkt
    
    # Set titler og labels
    ax.set_title('Koordinatsystemet')
    ax.set_xlabel('x-akse')
    ax.set_ylabel('y-akse')
    
    # Legge til rutenett
    ax.grid(True)
    
    # Vise plot
    plt.show()

# Eksempelbruk
print("Leksjon 7.1: Koordinatsystemet")
x = int(input("Skriv inn x-koordinaten til punktet: "))
y = int(input("Skriv inn y-koordinaten til punktet: "))
punkt = (x, y)
plot_koordinatsystem(punkt)