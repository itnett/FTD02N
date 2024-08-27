python?code_reference&code_event_index=3
import altair as alt

# Define and store the values
tykkelse_stav = 0.005  # Meter (5 mm)
tidspunkt1 = [0.1, 0.2]  # Sekunder (når hver stav bryter første fotoport)
tidspunkt2 = [0.3, 0.5]  # Sekunder (når hver stav bryter andre fotoport)

# Calculate hastigheter (velocities)
hastigheter = []
for i in range(2):
    delta_t = tidspunkt2[i] - tidspunkt1[i]
    hastigheter.append(tykkelse_stav / delta_t)

# Calculate akselerasjon (acceleration)
akselerasjon = (hastigheter[1] - hastigheter[0]) / (tidspunkt2[0] - tidspunkt1[0])

# Print results
print(f"Hastighet ved første fotoport: {hastigheter[0]:.2f} m/s")
print(f"Hastighet ved andre fotoport: {hastigheter[1]:.2f} m/s")
print(f"Gjennomsnittlig akselerasjon: {akselerasjon:.2f} m/s²")

# Create a DataFrame for plotting
import pandas as pd

df = pd.DataFrame({'Tidspunkt': tidspunkt1, 'Hastighet': hastigheter})

# Create the Altair chart
chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Tidspunkt:Q', axis=alt.Axis(title='Tid (s)')),
    y=alt.Y('Hastighet:Q', axis=alt.Axis(title='Hastighet (m/s)')),
    tooltip = ['Tidspunkt', 'Hastighet']
).properties(
    title='Hastighet vs. Tid'
).interactive()

# Save the chart as a JSON file
chart.save('hastighet_vs_tid.json')