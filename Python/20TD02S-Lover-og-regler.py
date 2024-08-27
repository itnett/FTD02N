python
import json

def generate_final_report():
    with open("verification_result.json") as f:
        verification_results = json.load(f)

    final_report = []
    for item, status in verification_results.items():
        final_report.append(f"{item}: {status}")

    with open("final_report.txt", "w") as f:
        f.write("\n".join(final_report))

if __name__ == "__main__":
    generate_final_report()