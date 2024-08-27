python
# This script prints the Greek alphabet using Unicode characters.
greek_alphabet = [
    'Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 
    'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 
    'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega'
]

greek_unicode = [
    '\u0391', '\u0392', '\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398', '\u0399',
    '\u039A', '\u039B', '\u039C', '\u039D', '\u039E', '\u039F', '\u03A0', '\u03A1', '\u03A3',
    '\u03A4', '\u03A5', '\u03A6', '\u03A7', '\u03A8', '\u03A9'
]

for name, char in zip(greek_alphabet, greek_unicode):
    print(f"{name}: {char}")