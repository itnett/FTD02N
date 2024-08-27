python
import json

def generate_report():
    with open("compliance_result.json") as f:
        results = json.load(f)

    report = []
    for regulation, status in results.items():
        report.append(f"{regulation}: {status}")

    with open("compliance_report.txt", "w") as f:
        f.write("\n".join(report))

if __name__ == "__main__":
    generate_report()