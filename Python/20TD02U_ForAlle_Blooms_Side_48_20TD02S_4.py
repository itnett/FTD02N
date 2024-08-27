python
frameworks = {
    'ISO 27001': ['Access Control', 'Asset Management', 'Cryptography'],
    'NIST CSF': ['Identify', 'Protect', 'Detect', 'Respond', 'Recover']
}

def compare_frameworks(frameworks):
    for framework, controls in frameworks.items():
        print(f"{framework}: {', '.join(controls)}")

compare_frameworks(frameworks)