python
def f(x):
    return x**2 + 2

def derivative_approximation(f, x, delta_x):
    return (f(x + delta_x) - f(x)) / delta_x

x_value = 0.5
delta_x = 0.1
tolerance = 0.00001

previous_derivative = derivative_approximation(f, x_value, delta_x)
delta_x /= 10
current_derivative = derivative_approximation(f, x_value, delta_x)

while abs(current_derivative - previous_derivative) > tolerance:
    previous_derivative = current_derivative
    delta_x /= 10
    current_derivative = derivative_approximation(f, x_value, delta_x)

print(f"Den deriverte til funksjonen i x = {x_value} er tilnærmet {current_derivative:.5f}")