python
import numpy as np

# Algebra: Basic Rules
print("Algebra: Basic Rules")
a, b, c = 1, 2, 3
expr1 = a + b + c
expr2 = a * b * c
print("Expression 1:", expr1)
print("Expression 2:", expr2)

# Fractions and Percentages
print("\nFractions and Percentages")
fraction = 3/4
percentage = fraction * 100
print(f"Fraction: {fraction}, Percentage: {percentage}%")

# Powers
print("\nPowers")
power = 2**3
print(f"2^3 = {power}")

# Standard Form
print("\nStandard Form")
standard_form = 5.67e8
print(f"Standard form of 5.67*10^8 is: {standard_form}")

# Simplification and Factorization
print("\nSimplification and Factorization")
from sympy import symbols, expand, factor
a, b = symbols('a b')
expr = a**2 - b**2
expanded_expr = expand(expr)
factored_expr = factor(expanded_expr)
print("Expanded expression:", expanded_expr)
print("Factored expression:", factored_expr)

# Solving Linear and Quadratic Equations
print("\nSolving Linear and Quadratic Equations")
from sympy import Eq, solve
x = symbols('x')
linear_eq = Eq(2*x - 4, 0)
quadratic_eq = Eq(x**2 - 5*x + 6, 0)
linear_solution = solve(linear_eq, x)
quadratic_solution = solve(quadratic_eq, x)
print("Linear equation solution:", linear_solution)
print("Quadratic equation solutions:", quadratic_solution)

# Solving Systems of Equations
print("\nSolving Systems of Equations")
y = symbols('y')
eq1 = Eq(2*x + y, 10)
eq2 = Eq(x - y, 2)
system_solution = solve((eq1, eq2), (x, y))
print("System of equations solution:", system_solution)

# Adjusting and Transforming Formulas
print("\nAdjusting and Transforming Formulas")
a, b, c = symbols('a b c')
formula = Eq(a*b, c)
transformed_formula = solve(formula, b)
print("Transformed formula:", transformed_formula)

# Trigonometry and Geometry
print("\nTrigonometry and Geometry")

# Area, Perimeter, Volume, and Surface Area
print("Area, Perimeter, Volume, and Surface Area")
rectangle_area = 5 * 3
rectangle_perimeter = 2 * (5 + 3)
cube_volume = 4**3
cube_surface_area = 6 * (4**2)
print(f"Rectangle area: {rectangle_area}, perimeter: {rectangle_perimeter}")
print(f"Cube volume: {cube_volume}, surface area: {cube_surface_area}")

# Pythagorean Theorem
print("\nPythagorean Theorem")
a, b = 3, 4
c = np.sqrt(a**2 + b**2)
print(f"For a right triangle with sides {a} and {b}, the hypotenuse is {c}")

# Trigonometry in Right Triangles
print("\nTrigonometry in Right Triangles")
angle = 30
opposite = 5
adjacent = opposite / np.tan(np.radians(angle))
print(f"For a 30 degree angle with opposite side {opposite}, the adjacent side is {adjacent}")

# Vectors in the Plane
print("\nVectors in the Plane")
vector1 = np.array([2, 3])
vector2 = np.array([1, 4])
vector_sum = vector1 + vector2
print(f"Vector 1: {vector1}, Vector 2: {vector2}, Sum: {vector_sum}")

# Functions

# Straight Lines
print("\nFunctions: Straight Lines")
x = np.linspace(-10, 10, 400)
y = 2*x + 3
print(f"y = 2x + 3 for x in range -10 to 10")

# Polynomial Functions
print("\nPolynomial Functions")
x = np.linspace(-10, 10, 400)
poly_function = x**3 - 6*x**2 + 11*x - 6
print(f"Polynomial function evaluated over range: {poly_function}")

# Exponential Functions
print("\nExponential Functions")
x = np.linspace(0, 10, 400)
exp_function = np.exp(x)
print(f"Exponential function evaluated over range: {exp_function}")

# Differentiation of Polynomial Functions
print("\nDifferentiation of Polynomial Functions")
from sympy import diff
x = symbols('x')
poly_function = x**3 - 6*x**2 + 11*x - 6
poly_diff = diff(poly_function, x)
print(f"Derivative of the polynomial function: {poly_diff}")

# Regression using Digital Tools (e.g., numpy)
print("\nRegression using Digital Tools")
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 4, 9, 16, 25])
coefficients = np.polyfit(x_data, y_data, 2)
poly_fit = np.poly1d(coefficients)
print(f"Polynomial fit: {poly_fit}")

# Introductory Physics Topics

# SI System and Decimal Prefixes
print("\nIntroductory Physics: SI System and Decimal Prefixes")
mass_kg = 5  # kilograms
mass_g = mass_kg * 1000  # grams
print(f"Mass: {mass_kg} kg = {mass_g} g")

# Concepts of Mass, Weight, and Density
print("\nConcepts of Mass, Weight, and Density")
mass = 10  # kg
volume = 2  # m^3
density = mass / volume
print(f"Density: {density} kg/m^3")

# Uncertainty and Significant Figures
print("\nUncertainty and Significant Figures")
measurement = 5.678  # example measurement
uncertainty = 0.01  # example uncertainty
print(f"Measurement: {measurement} ± {uncertainty}")

# Force and Linear Motion

# Applying Newton's Laws
print("\nApplying Newton's Laws")
mass = 10  # kg
force = mass * 9.81  # F = ma (assuming g = 9.81 m/s^2)
print(f"Force: {force} N")

# Calculating with Motion Equations at Constant Speed and Acceleration
print("\nMotion Equations at Constant Speed and Acceleration")
initial_velocity = 0  # m/s
final_velocity = 20  # m/s
time = 5  # s
acceleration = (final_velocity - initial_velocity) / time
print(f"Acceleration: {acceleration} m/s^2")

# Energy

# Calculating Work, Power, and Efficiency
print("\nCalculating Work, Power, and Efficiency")
force = 10  # N
distance = 5  # m
work = force * distance
power = work / time
output_energy = 50  # Example value
input_energy = 100  # Example value
efficiency = (output_energy / input_energy) * 100
print(f"Work: {work} J, Power: {power} W, Efficiency: {efficiency}%")

# Calculating Kinetic and Potential Energy
print("\nCalculating Kinetic and Potential Energy")
mass = 10  # kg
velocity = 15  # m/s
kinetic_energy = 0.5 * mass * velocity**2
height = 20  # m
potential_energy = mass * 9.81 * height
print(f"Kinetic Energy: {kinetic_energy} J, Potential Energy: {potential_energy} J")

# Applying Energy Conservation
print("\nApplying Energy Conservation")
total_energy_initial = kinetic_energy + potential_energy  # assuming no other forms of energy
total_energy_final = total_energy_initial  # assuming energy conservation
print(f"Total Initial Energy: {total_energy_initial} J, Total Final Energy: {total_energy_final} J")

# First Law of Thermodynamics
print("\nFirst Law of Thermodynamics")
work_done = 100  # Example value in J
heat_added = 50  # Example value in J
internal_energy_change = work_done + heat_added
print(f"Change in Internal Energy: {internal_energy_change} J")

# Specialized Study Topics

# Briggs Logarithms
print("\nBriggs Logarithms")
log_value = np.log10(1000)
print(f"Log10 of 1000: {log_value}")

# Combinatorics
print("\nCombinatorics")
from math import factorial
n = 5
r = 3
combinations = factorial(n) / (factorial(r) * factorial(n - r))
print(f"Combinations of 5 taken 3 at a time: {combinations}")

# Probability and Statistics
print("\nProbability and Statistics")
probability = 1 / 6  # rolling a

 die and getting a specific number
print(f"Probability of rolling a 3 on a die: {probability}")

# Phases and Phase Transitions
print("\nPhases and Phase Transitions")
melting_point = 0  # degrees Celsius
print(f"Melting point of water: {melting_point}°C")

# Heat and Internal Energy
print("\nHeat and Internal Energy")
specific_heat = 4.18  # J/g°C for water
mass = 100  # g
temperature_change = 20  # °C
heat_energy = specific_heat * mass * temperature_change
print(f"Heat Energy: {heat_energy} J")

# Second Law of Thermodynamics
print("\nSecond Law of Thermodynamics")
temperature = 25  # degrees Celsius
entropy_change = heat_energy / (temperature + 273.15)  # assuming temperature in Celsius
print(f"Entropy Change: {entropy_change} J/K")

# Heat Capacity and Calorimetry
print("\nHeat Capacity and Calorimetry")
heat_capacity = specific_heat * mass
print(f"Heat Capacity: {heat_capacity} J/°C")

# Number Systems
print("\nNumber Systems")
binary_number = bin(10)
decimal_number = 10
hexadecimal_number = hex(10)
print(f"Binary: {binary_number}, Decimal: {decimal_number}, Hexadecimal: {hexadecimal_number}")

# Algorithmic Thinking
print("\nAlgorithmic Thinking")
# Example of a simple algorithm: Euclidean algorithm to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"GCD of 48 and 18: {gcd(48, 18)}")

# Boolean Algebra
print("\nBoolean Algebra")
a = True
b = False
and_operation = a and b
or_operation = a or b
print(f"AND operation: {and_operation}, OR operation: {or_operation}")

# Simple Algorithm Programming
print("\nSimple Algorithm Programming")
# Example: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}")