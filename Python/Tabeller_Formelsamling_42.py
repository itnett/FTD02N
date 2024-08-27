python
# Define points P and Q
xP, yP, zP = sp.symbols('xP yP zP')
xQ, yQ, zQ = sp.symbols('xQ yQ zQ')

# Vector PQ
vector_PQ = sp.Matrix([xQ - xP, yQ - yP, zQ - zP])
print(f"Vector PQ: {vector_PQ[0]}i + {vector_PQ[1]}j + {vector_PQ[2]}k")