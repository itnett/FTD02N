python
def significant_figures(value=1234.567, significant_digits=4):
    """
    Round a value to a specified number of significant digits.
    
    Parameters:
    value (float): The value to round.
    significant_digits (int): The number of significant digits.
    
    Returns:
    float: The value rounded to the specified number of significant digits.
    """
    from decimal import Decimal
    rounded_value = round(Decimal(value), significant_digits - 1 - int(Decimal(value).adjusted()))
    print(f"Verdi: {value} avrundet til {significant_digits} gjeldende siffer er {rounded_value}")
    return rounded_value

# Example usage
significant_figures()