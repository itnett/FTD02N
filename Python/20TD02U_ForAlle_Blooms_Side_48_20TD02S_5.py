python
laws = {
    'GDPR': 'General Data Protection Regulation, applicable in the EU.',
    'CCPA': 'California Consumer Privacy Act, applicable in California, USA.'
}

def search_law(law_name):
    return laws.get(law_name, "Law not found.")

print(search_law('GDPR'))