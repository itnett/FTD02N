python
import numpy as np

# Potenser
tall = 2
eksponent = 5
resultat = tall**eksponent
print(f"{tall} opphøyd i {eksponent} er:", resultat)

# Tall på standardform
stort_tall = 123456789
standardform = "{:.2e}".format(stort_tall)
print("Standardform:", standardform)