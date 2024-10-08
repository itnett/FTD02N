python
threats = {
    'Malware': 'Software designed to disrupt, damage, or gain unauthorized access to a system.',
    'Phishing': 'A method of trying to gather personal information using deceptive e-mails and websites.',
    'DDoS': 'Distributed Denial of Service, a type of attack where multiple compromised systems are used to target a single system.'
}

def display_threats():
    for threat, description in threats.items():
        print(f"{threat}: {description}")

display_threats()