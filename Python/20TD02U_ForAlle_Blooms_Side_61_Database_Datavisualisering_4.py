python
import plotly.express as px
import plotly.graph_objects as go

# Eksempeldata
df = px.data.gapminder().query("country=='Norway'")

# Lag et interaktivt linjediagram som viser BNP over tid
fig = px.line(df, x='year', y='gdpPercap', title='BNP per capita over tid i Norge')
fig.show()

# Legg til flere visualiseringer som scatter plot og histogram for å analysere andre aspekter