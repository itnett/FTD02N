python
def product_market_strategy(products=['Product A', 'Product B'], markets=['Market 1', 'Market 2'], channels=['Online', 'Retail']):
    """
    Develop a strategy for product, market, and distribution channel selection.

    Parametere:
    products (list): Liste over produkter
    markets (list): Liste over markeder
    channels (list): Liste over distribusjonskanaler

    Returnerer:
    None
    """
    print("Products:")
    for product in products:
        print(f"- {product}")
    print("\nMarkets:")
    for market in markets:
        print(f"- {market}")
    print("\nDistribution Channels:")
    for channel in channels:
        print(f"- {channel}")

# Eksempel på bruk
product_market_strategy()