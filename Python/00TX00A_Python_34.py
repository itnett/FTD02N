python
def customer_behavior_analysis(market='B2C', behavior_factors=['Price', 'Quality', 'Brand Loyalty']):
    """
    Analyze customer behavior in a given market.

    Parametere:
    market (str): Markedstype ('B2C' eller 'B2B')
    behavior_factors (list): Liste over faktorer som påvirker kjøpsatferd

    Returnerer:
    None
    """
    print(f"Market: {market}")
    print("Customer Behavior Factors:")
    for factor in behavior_factors:
        print(f"- {factor}")

# Eksempel på bruk
customer_behavior_analysis()