python
print("\nRegression using Digital Tools")
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1, 4, 9, 16, 25])
coefficients = np.polyfit(x_data, y_data, 2)
poly_fit = np.poly1d(coefficients)
print(f"Polynomial fit: {poly_fit}")