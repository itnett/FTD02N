python
import json

def propose_actions():
    with open("compliance_result.json") as f:
        results = json.load(f)

    actions = {}
    for service, compliance in results.items():
        for item, status in compliance.items():
            if status == "Non-compliant":
                actions[item] = "Corrective action needed"

    with open("corrective_actions.json", "w") as f:
        json.dump(actions, f)

if __name__ == "__main__":
    propose_actions()