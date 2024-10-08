python
risks = {
    'Malware': {'Probability': 0.8, 'Impact': 0.9},
    'Phishing': {'Probability': 0.7, 'Impact': 0.5},
    'DDoS': {'Probability': 0.4, 'Impact': 0.7}
}

def calculate_risk(risks):
    for threat, metrics in risks.items():
        risk = metrics['Probability'] * metrics['Impact']
        print(f"Risk level for {threat}: {risk}")

calculate_risk(risks)