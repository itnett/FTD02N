python
import plotly.express as px

# Lag flere visualiseringer og sammenlign dem
fig1 = px.histogram(tips, x='total_bill', title='Histogram over total regning')
fig2 = px.box(tips, x='day', y='total_bill', title='Boksplott over total regning per dag')
fig1.show()
fig2.show()

# Sammenlign brukernes forståelse av dataene mellom de forskjellige visualiseringene.