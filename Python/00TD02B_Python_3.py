python
def ethical_decision_simulation(scenarios=["Data privacy concern", "Conflict of interest"], decisions=["Report to supervisor", "Address privately"]):
    """
    Simulate ethical decision-making.
    
    Parameters:
    scenarios (list): List of ethical scenarios.
    decisions (list): List of potential decisions.
    
    Returns:
    None
    """
    for scenario in scenarios:
        print(f"Scenario: {scenario}")
        for i, decision in enumerate(decisions, 1):
            print(f"{i}. {decision}")
        print()

# Example usage
ethical_decision_simulation()