python
import pandas as pd
import matplotlib.pyplot as plt

# Data fra resultatregnskapet og balansen
resultatregnskap = {
    "Post": ["Salgsinntekter", "Andre driftsinntekter", "Sum driftsinntekter", "Varekostnad", 
             "Lønnskostnader", "Ordinære avskrivninger", "Andre driftskostnader", "Sum driftskostnader", 
             "Driftsresultat", "Finansinntekter", "Finanskostnader", "Resultat før skatt", "Skatt", "Årsresultat"],
    "2022": [119914, 0, 119914, 66306, 40404, 145, 11349, 118204, 1710, 21, 62, 1669, 450, 1219],
    "2021": [82354, 0, 82354, 32031, 33660, 319, 9759, 75769, 6585, 15, 73, 6527, 1455, 5072]
}

balanse = {
    "Post": ["Anleggsmidler", "Varelager", "Kundefordringer", "Kasse/bank", "Sum omløpsmidler", "Sum eiendeler", 
             "Aksjekapital", "Annen egenkapital", "Sum egenkapital", "Langsiktig gjeld", "Leverandørgjeld", 
             "Skyldig offentlige avgifter", "Utbytte", "Annen kortsiktig gjeld", "Sum kortsiktig gjeld", "Sum gjeld", 
             "Sum egenkapital og gjeld"],
    "2022": [690, 560, 27196, 26963, 54719, 55409, 1000, 24995, 25995, 4296, 4001, 6026, 0, 15091, 25118, 29414, 55409],
    "2021": [821, 643, 22844, 27369, 50856, 51677, 1000, 26214, 27214, 5186, 4394, 3474, 0, 11409, 19277, 24463, 51677]
}

df_resultat = pd.DataFrame(resultatregnskap)
df_balanse = pd.DataFrame(balanse)

display(df_resultat)
display(df_balanse)