python
def investment_proposal():
    """
    Propose an investment to reduce costs and improve efficiency.
    """
    investment_description = "Investing in a new automated production line"
    estimated_cost = 500000  # Example cost in NOK
    expected_savings_per_year = 100000  # Example savings per year in NOK
    
    print("Investment Proposal:")
    print(f"Description: {investment_description}")
    print(f"Estimated Cost: {estimated_cost} NOK")
    print(f"Expected Savings per Year: {expected_savings_per_year} NOK")
    
    return investment_description, estimated_cost, expected_savings_per_year

# Example usage
investment_proposal()