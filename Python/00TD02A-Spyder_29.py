python
   tangent = sp.diff(f, x).subs(x, 1) * (x - 1) + f.subs(x, 1)