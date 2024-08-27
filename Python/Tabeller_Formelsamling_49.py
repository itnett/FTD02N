python
# Normal vector coefficients
alpha, beta, gamma = N
delta = -N.dot(sp.Matrix([a1, a2, a3]))

# Distance from point P to the plane
distance_to_plane = sp.Abs(alpha*p1 + beta*p2 + gamma*p3 + delta) / sp.sqrt(alpha**2 + beta**2 + gamma**2)

print(f"Distance from point P to the plane: {distance_to_plane}")