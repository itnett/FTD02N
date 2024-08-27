python
import math

def caesar_kryptering(tekst, forskyvning):
    kryptert_tekst = ""
    for bokstav in tekst:
        if bokstav.isalpha():
            base = ord('a') if bokstav.islower() else ord('A')
            kryptert_bokstav = chr((ord(bokstav) - base + forskyvning) % 26 + base)
            kryptert_tekst += kryptert_bokstav
        else:
            kryptert_tekst += bokstav
    return kryptert_tekst

klartekst = "Hei, verden!"
forskyvning = 3
kryptert_tekst = caesar_kryptering(klartekst, forskyvning)
print(kryptert_tekst)  # Output: "Khl, åoguhu!"