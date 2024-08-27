python
import plotly.express as px
import pandas as pd

# Last inn eksempeldata
df = px.data.iris()

# Lag en scatter plot
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 title="Iris Dataset - Sepal Width vs Sepal Length")

# Vis plot
fig.show()