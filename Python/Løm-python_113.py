python
# Beregne lønnskostnad for planlagte timer
planlagte_timer = 25
faktiske_timer = 30
inntakskost_materiell = 13500
overtidstimer = 5

planlagt_lønnskost = planlagte_timer * variabel_lønnskostnad
faktisk_lønnskost = (faktiske_timer - overtidstimer) * variabel_lønnskostnad + overtidstimer * variabel_lønnskostnad * 2

planlagt_total_kost = planlagt_lønnskost + 15000
faktisk_total_kost = faktisk_lønnskost + inntakskost_materiell

avvik_total_kost = faktisk_total_kost - planlagt_total_kost

print(f"Planlagt total kostnad: {planlagt_total_kost:.2f} kr")
print(f"Faktisk total kostnad: {faktisk_total_kost:.2f} kr")
print(f"Avvik i total kostnad: {avvik_total_kost:.2f} kr")