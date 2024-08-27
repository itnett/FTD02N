python
  # Enkel kalkulator i Python
  def add(x, y):
      return x + y

  def subtract(x, y):
      return x - y

  def multiply(x, y):
      return x * y

  def divide(x, y):
      if y != 0:
          return x / y
      else:
          return "Error! Division by zero."

  # Brukerinput
  print("Velkommen til kalkulatoren!")
  num1 = float(input("Skriv inn første tall: "))
  num2 = float(input("Skriv inn andre tall: "))

  print("Velg operasjon:")
  print("1. Legg til")
  print("2. Trekk fra")
  print("3. Multipliser")
  print("4. Del")

  choice = input("Velg operasjon (1/2/3/4): ")

  if choice == '1':
      print(f"Resultat: {add(num1, num2)}")
  elif choice == '2':
      print(f"Resultat: {subtract(num1, num2)}")
  elif choice == '3':
      print(f"Resultat: {multiply(num1, num2)}")
  elif choice == '4':
      print(f"Resultat: {divide(num1, num2)}")
  else:
      print("Ugyldig valg")