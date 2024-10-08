python
def swot_analysis(styrker, svakheter, muligheter, trusler):
    """
    Lager en enkel SWOT-analyse.

    Parametere:
    styrker (list): Liste over styrker
    svakheter (list): Liste over svakheter
    muligheter (list): Liste over muligheter
    trusler (list): Liste over trusler

    Returnerer:
    dict: En ordbok med SWOT-analyse
    """
    swot = {
        'Styrker': styrker,
        'Svakheter': svakheter,
        'Muligheter': muligheter,
        'Trusler': trusler
    }
    return swot

# Eksempel på bruk
swot = swot_analyse(
    styrker=['Godt omdømme', 'Høy kompetanse'],
    svakheter=['Høye kostnader', 'Begrenset markedsføring'],
    muligheter=['Nye markeder', 'Teknologiske fremskritt'],
    trusler=['Økt konkurranse', 'Økonomisk nedgang']
)
for kategori, punkter i swot.items():
    print(f'{kategori}:')
    for punkt i punkter:
        print(f' - {punkt}')