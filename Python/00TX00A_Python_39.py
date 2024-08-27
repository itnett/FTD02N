python
def leadership_strategy():
    """
    Definerer strategier for å lede en organisasjon effektivt og bærekraftig.
    """
    strategies = {
        "Efficiency": [
            "Implement lean management principles",
            "Automate repetitive tasks",
            "Optimize resource allocation"
        ],
        "Work Environment": [
            "Promote open communication",
            "Ensure work-life balance",
            "Provide professional development opportunities"
        ],
        "Sustainability": [
            "Adopt green technologies",
            "Reduce waste and emissions",
            "Support sustainable suppliers"
        ],
        "Social Responsibility": [
            "Engage in community service",
            "Ensure ethical labor practices",
            "Promote diversity and inclusion"
        ]
    }
    return strategies

# Eksempel på bruk
strategies = leadership_strategy()
for category, items in strategies.items():
    print(f"{category}:")
    for item in items:
        print(f" - {item}")