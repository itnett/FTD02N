python
def investment_analysis(initial_investment=100000, annual_cash_flows=[20000, 30000, 40000, 50000, 60000], discount_rate=0.1):
    """
    Perform an investment analysis using Net Present Value (NPV).
    
    Parameters:
    initial_investment (float): The initial investment amount.
    annual_cash_flows (list): List of annual cash flows.
    discount_rate (float): Discount rate for NPV calculation.
    
    Returns:
    float: Net Present Value (NPV).
    """
    npv = -initial_investment
    for t, cash_flow in enumerate(annual_cash_flows, start=1):
        npv += cash_flow / ((1 + discount_rate) ** t)
    
    print(f"Net Present Value (NPV) of the investment: {npv}")
    return npv

# Eksempel på bruk
investment_analysis()