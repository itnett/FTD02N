python
import json

def propose_actions():
    with open("compliance_result.json") as f:
        results = json.load(f)

    actions = {}
    for regulation, status in results.items():
        if status[regulation] == "Non-compliant":
            actions[regulation] = "Corrective action needed"

    with open("corrective_actions.json", "w") as f:
        json.dump(actions, f)

if __name__ == "__main__":
    propose_actions()