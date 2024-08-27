python
import math

def briggs_logarithms(value=1000):
    """
    Calculate the Briggs logarithm (base 10) of a given value.
    
    Parameters:
    value (float): The value for which to calculate the logarithm.
    
    Returns:
    float: The logarithm (base 10) of the value.
    """
    log_value = math.log10(value)
    print(f"Briggs logaritme (base 10) av {value} er {log_value}")
    return log_value

# Example usage
briggs_logarithms()