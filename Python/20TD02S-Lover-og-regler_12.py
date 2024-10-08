python
import json

def generate_report():
    with open("compliance_result.json") as f:
        results = json.load(f)

    report = []
    for service, compliance in results.items():
        report.append(f"{service} Compliance Report:")
        for item, status in compliance.items():
            report.append(f"{item}: {status}")

    with open("compliance_report.txt", "w") as f:
        f.write("\n".join(report))

if __name__ == "__main__":
    generate_report()