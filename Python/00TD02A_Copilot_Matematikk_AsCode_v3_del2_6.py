python
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="StudyProgram"
)

# Query the total costs for each lab type
query = """
SELECT lab_type, 
       estimated_time * hourly_rate + hardware_cost + service_cost AS total_cost 
FROM VirtualLabCosts;
"""

# Load data into a DataFrame
df = pd.read_sql(query, conn)

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['lab_type'], df['total_cost'], color='blue')
plt.xlabel('Lab Type')
plt.ylabel('Total Cost')
plt.title('Total Cost of Setting Up Different Virtual Labs')
plt.show()