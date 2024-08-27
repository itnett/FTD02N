python
# Grunnleggende representasjon av ER-diagram-komponenter
entiteter = ['Student', 'Kurs', 'Lærer']
relasjoner = [('Student', 'Registrerer seg', 'Kurs'), ('Lærer', 'Underviser', 'Kurs')]

print("Entiteter:")
for enhet in entiteter:
    print(f"- {enhet}")

print("\nRelasjoner:")
for relasjon in relasjoner:
    print(f"- {relasjon[0]} {relasjon[1]} {relasjon[2]}")