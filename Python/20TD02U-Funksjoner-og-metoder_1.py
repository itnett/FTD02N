python
class Hund:
  def __init__(self, navn):
    self.navn = navn

  def bjeff(self):
    print("Voff! Jeg heter", self.navn)

min_hund = Hund("Fido")
min_hund.bjeff()  # Output: Voff! Jeg heter Fido