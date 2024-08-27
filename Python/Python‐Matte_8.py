python
import sympy as sp

def factor_expression(expr='x**2 - 4'):
    """
    Factor a given algebraic expression.
    
    Parameters:
    expr (str): The algebraic expression to be factored.
    """
    x = sp.symbols('x')
    expression = sp.sympify(expr)
    factored_expression = sp.factor(expression)
    print(f"Faktorisering av {expr}: {factored_expression}")
    print(f"GeoGebra input: Factor[{expr}]")

# Example usage
factor_expression()