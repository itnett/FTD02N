python
arbeidstimer = 25
materiell_kost = 15000
materiell_påslag = 0.10
fortjeneste_påslag = 0.10

arbeid_kost = arbeidstimer * selvkost_per_time
materiell_kost_med_påslag = materiell_kost * (1 + materiell_påslag)
selvkost = arbeid_kost + materiell_kost_med_påslag
fortjeneste = selvkost * fortjeneste_påslag
salgspris_uten_mva = selvkost + fortjeneste
mva = salgspris_uten_mva * 0.25
salgspris_med_mva = salgspris_uten_mva + mva

print(f"Arbeid: {arbeid_kost:.2f} kr")
print(f"Materiell: {materiell_kost_med_påslag:.2f} kr")
print(f"Selvkost: {selvkost:.2f} kr")
print(f"Fortjeneste: {fortjeneste:.2f} kr")
print(f"Salgspris uten mva: {salgspris_uten_mva:.2f} kr")
print(f"Mva: {mva:.2f} kr")
print(f"Salgspris med mva: {salgspris_med_mva:.2f} kr")