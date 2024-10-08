python
def beregn_geometri(form, *mål):
    if form == "sirkel":
        radius = mål[0]
        areal = math.pi * radius**2
        omkrets = 2 * math.pi * radius
    elif form == "rektangel":
        lengde, bredde = mål
        areal = lengde * bredde
        omkrets = 2 * (lengde + bredde)
    else:
        raise ValueError("Ukjent form!")
    return areal, omkrets

# Brukerinput: "sirkel", radius = 5
print(beregn_geometri("sirkel", 5))  # Output: (78.54, 31.42)