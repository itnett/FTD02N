python
def tverrkulturell_innsikt(spørsmål):
    svar = {
        "Hva er viktigheten av høflighet i Japan?": "Høflighet er svært viktig i japansk kultur. Det er viktig å vise respekt, spesielt i formelle situasjoner.",
        "Hva betyr 'deadline' på engelsk?": "'Deadline' refererer til den siste datoen eller tiden noe må være fullført."
    }
    return svar.get(spørsmål, "Beklager, jeg har ikke innsikt i dette spørsmålet.")

print(tverrkulturell_innsikt("Hva er viktigheten av høflighet i Japan?"))