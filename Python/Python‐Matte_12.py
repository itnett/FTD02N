python
import math

def pythagorean_theorem(a=3, b=4):
    """
    Calculate the hypotenuse of a right triangle using Pythagoras' theorem.
    
    Parameters:
    a (float): One leg of the triangle.
    b (float): The other leg of the triangle.
    
    Returns:
    c (float): The hypotenuse of the triangle.
    """
    c = math.sqrt(a**2 + b**2)
    print(f"Med sidene a={a} og b={b} er hypotenusen c={c}")
    print(f"GeoGebra input: c = sqrt({a}^2 + {b}^2)")
    return c

def trigonometry_right_triangle(angle_degrees=30, hypotenuse=1):
    """
    Calculate the lengths of the legs of a right triangle given an angle and the hypotenuse.
    
    Parameters:
    angle_degrees (float): Angle in degrees.
    hypotenuse (float): The hypotenuse of the triangle.
    
    Returns:
    (float, float): The lengths of the opposite and adjacent sides.
    """
    angle_radians = math.radians(angle_degrees)
    opposite = hypotenuse * math.sin(angle_radians)
    adjacent = hypotenuse * math.cos(angle_radians)
    
    print(f"Med hypotenusen {hypotenuse} og vinkelen {angle_degrees} grader er:")
    print(f"Motstående side = {opposite}")
    print(f"Tilstøtende side = {adjacent}")
    print(f"GeoGebra input: sin({angle_degrees}) = {opposite}/{hypotenuse}, cos({angle_degrees}) = {adjacent}/{hypotenuse}")
    return opposite, adjacent

# Example usage
pythagorean_theorem()
trigonometry_right_triangle()