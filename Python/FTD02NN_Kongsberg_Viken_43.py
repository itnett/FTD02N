python
  class BankAccount:
      def __init__(self, owner, balance=0):
          self.owner = owner
          self.balance = balance

      def deposit(self, amount):
          if amount > 0:
              self.balance += amount
              print(f"Innskudd: {amount} | Ny saldo: {self.balance}")
          else:
              print("Beløpet må være positivt!")

      def withdraw(self, amount):
          if 0 < amount <= self.balance:
              self.balance -= amount
              print(f"Uttak: {amount} | Ny saldo: {self.balance}")
          else:
              print("Ugyldig beløp eller ikke nok saldo!")

      def display_balance(self):
          print(f"Kontoeier: {self.owner} | Saldo: {self.balance}")

  # Bruk av klassen
  account = BankAccount("Per", 1000)
  account.deposit(500)
  account.withdraw(200)
  account.display_balance()