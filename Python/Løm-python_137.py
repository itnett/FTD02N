python
import numpy as np

kontantstrømmer = [-50000, 15000, 20000, 25000, 30000]
irr = np.irr(kontantstrømmer)
print(f"Internrente (IRR): {irr:.2%}")