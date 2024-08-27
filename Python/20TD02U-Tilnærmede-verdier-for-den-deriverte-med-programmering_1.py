python
# Testing med delta_x = 0.01 og delta_x = 0.001
x_value = 0.5
delta_x_values = [0.01, 0.001]

for delta_x in delta_x_values:
    approx_derivative = derivative_approximation(f, x_value, delta_x)
    print(f"Tilnærmet verdi for den deriverte ved delta_x = {delta_x}: {approx_derivative:.5f}")