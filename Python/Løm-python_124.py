python
def beregn_driftsmargin(driftsinntekter, driftskostnader):
    driftsresultat = driftsinntekter - driftskostnader
    driftsmargin = (driftsresultat / driftsinntekter) * 100
    return driftsmargin

driftsinntekter = 500000
driftskostnader = 350000
driftsmargin = beregn_driftsmargin(driftsinntekter, driftskostnader)
print(f"Driftsmargin: {driftsmargin:.2f}%")