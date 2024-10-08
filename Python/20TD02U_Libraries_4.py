python
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the mean age
mean_age = df['Age'].mean()
print("\nMean Age:", mean_age)

# Filter employees with salary greater than 75000
high_salary = df[df['Salary'] > 75000]
print("\nEmployees with salary > 75000:")
print(high_salary)

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus:")
print(df)