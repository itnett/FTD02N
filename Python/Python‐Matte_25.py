python
import math

def combinations(n=5, k=2):
    """
    Calculate the number of combinations (n choose k).
    
    Parameters:
    n (int): Total number of items.
    k (int): Number of items to choose.
    
    Returns:
    int: Number of combinations.
    """
    comb = math.comb(n, k)
    print(f"Antall kombinasjoner av {n} gjenstander tatt {k} av gangen er {comb}")
    return comb

# Example usage
combinations()