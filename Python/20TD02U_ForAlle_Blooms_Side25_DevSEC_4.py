python
import html

# Escape brukerinput før det vises
navn = html.escape(input("Skriv inn navn: "))
print(f"<h1>Velkommen, {navn}!</h1>")