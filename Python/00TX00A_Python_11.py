python
def swot_analysis():
    """
    Perform a SWOT analysis for a hypothetical company.
    """
    strengths = [
        "Strong reputation for timely delivery",
        "Competent leadership",
        "Solid equity",
        "High employee satisfaction",
    ]
    weaknesses = [
        "High operational costs",
        "Dependence on current market conditions",
        "Limited market diversification",
    ]
    opportunities = [
        "Potential for product development",
        "Exploring new markets",
        "Technological advancements",
    ]
    threats = [
        "Increasing costs",
        "Economic downturn",
        "Health and productivity issues among employees",
    ]
    
    print("SWOT Analysis:")
    print("\nStrengths:")
    for s in strengths:
        print(f"- {s}")
    print("\nWeaknesses:")
    for w in weaknesses:
        print(f"- {w}")
    print("\nOpportunities:")
    for o in opportunities:
        print(f"- {o}")
    print("\nThreats:")
    for t in threats:
        print(f"- {t}")

# Example usage
swot_analysis()