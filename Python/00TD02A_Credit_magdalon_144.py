python
# ... (kode fra forrige eksempel)

# Deriver responstid-funksjonen
d_responstid = diff(responstid_funksjon, brukere)

# Finn ekstremalpunktet (minimum)
min_brukere = solveset(d_responstid, brukere, domain=S.Reals)
min_responstid = responstid_lambda(min_brukere.args[0])  # .args[0] henter ut verdien fra løsningsmengden

print(f"Minimum responstid: {min_responstid:.2f} ms ved {min_brukere.args[0]} brukere")