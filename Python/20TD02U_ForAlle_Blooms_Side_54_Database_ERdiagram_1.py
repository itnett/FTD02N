python
# Representasjon av ER-diagram med kardinalitet
relasjoner_med_kardinalitet = [
    ('Student', 'Registrerer seg i', 'Kurs', '1:M'),
    ('Lærer', 'Underviser', 'Kurs', '1:M')
]

print("Relasjoner med Kardinalitet:")
for relasjon in relasjoner_med_kardinalitet:
    print(f"- {relasjon[0]} {relasjon[1]} {relasjon[2]} ({relasjon[3]})")