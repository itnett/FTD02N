python
# Logisk design for et ER-diagram med flere tabeller og relasjoner
entiteter = ['Student', 'Kurs', 'Lærer', 'Karakter']
relasjoner = [
    ('Student', 'Registrerer seg i', 'Kurs', '1:M'),
    ('Lærer', 'Underviser', 'Kurs', '1:M'),
    ('Student', 'Mottar', 'Karakter', '1:M')
]

print("Entiteter:")
for enhet in entiteter:
    print(f"- {enhet}")

print("\nRelasjoner med Kardinalitet:")
for relasjon in relasjoner:
    print(f"- {relasjon[0]} {relasjon[1]} {relasjon[2]} ({relasjon[3]})")