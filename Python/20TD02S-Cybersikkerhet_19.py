python
def calculate_risk(likelihood, impact):
    return likelihood * impact

risks = [
    {'name': 'Phishing', 'likelihood': 0.8, 'impact': 0.7},
    {'name': 'Malware', 'likelihood': 0.6, 'impact': 0.9},
]

for risk in risks:
    risk_score = calculate_risk(risk['likelihood'], risk['impact'])
    print(f"Risiko: {risk['name']}, Score: {risk_score}")