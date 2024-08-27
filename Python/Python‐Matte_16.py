python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def perform_linear_regression(x_data=[1, 2, 3, 4, 5], y_data=[2, 4, 5, 4, 5]):
    """
    Perform linear regression on a set of data points and plot the result.
    
    Parameters:
    x_data (list): List of x-coordinates of the data points.
    y_data (list): List of y-coordinates of the data points.
    """
    x = np.array(x_data).reshape(-1, 1)
    y = np.array(y_data)
    
    model = LinearRegression()
    model.fit(x, y)
    
    y_pred = model.predict(x)
    
    plt.scatter(x, y, color='blue', label='Data points')
    plt.plot(x, y_pred, color='red', label='Linear regression line')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Linear Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for data points: List of points (x, y)")
    print(f"GeoGebra input for regression line: y = {model.coef_[0]}*x + {model.intercept_}")

# Example usage
perform_linear_regression()