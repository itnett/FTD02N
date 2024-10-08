python?code_reference&code_event_index=3
import altair as alt
import numpy as np
import pandas as pd

# 1. Phase Diagram for a Web Server
# Generate data
np.random.seed(42)  # for reproducibility
data = pd.DataFrame({
    'load': np.random.uniform(0, 200, 1000),
    'response_time': np.random.uniform(0, 10, 1000)
})

# Define server states based on thresholds
def get_server_state(load, response_time):
    if load < 100 and response_time < 2:
        return "Normal"
    elif 100 <= load < 180 and response_time < 5:
        return "Overloaded"
    else:
        return "Crash"

data['server_state'] = data.apply(lambda row: get_server_state(row['load'], row['response_time']), axis=1)

# Create the chart
chart1 = alt.Chart(data).mark_circle().encode(
    x='load',
    y='response_time',
    color='server_state:N',
    tooltip=['load', 'response_time', 'server_state']
).properties(
    title='Web Server Phase Diagram'
).interactive()

chart1.save('web_server_phase_diagram.json')

# 2. State Diagram for a Firewall
states = {'Blocking': (0, 1), 'Allowing': (1, 1), 'Logging': (0.5, 0)}
transitions = [('Blocking', 'Allowing'), ('Allowing', 'Logging'), ('Logging', 'Blocking')]

# Data for nodes (states)
nodes_data = pd.DataFrame(list(states.items()), columns=['state', 'position'])

# Data for edges (transitions)
edges_data = pd.DataFrame(transitions, columns=['source', 'target'])

# Base chart for nodes
base = alt.Chart(nodes_data).encode(
    x=alt.X('position:Q', axis=alt.Axis(title='')),
    y=alt.Y('position:Q', axis=alt.Axis(title=''))
)

# Points for states
points = base.mark_point(size=500, filled=True).encode(
    tooltip=['state:N']
)

# Text labels for states
text = base.mark_text(align='center', baseline='middle', dy=-5).encode(
    text='state:N'
)

# Links for transitions
links = alt.Chart(edges_data).mark_line(point=True).encode(
    x=alt.X('source:Q', axis=alt.Axis(title='')),
    y=alt.Y('source:Q', axis=alt.Axis(title='')),
    x2=alt.X2('target:Q'),
    y2=alt.Y2('target:Q')
).transform_lookup(
    lookup='source',
    from_=alt.LookupData(nodes_data, 'state', ['position'])
).transform_lookup(
    lookup='target',
    from_=alt.LookupData(nodes_data, 'state', ['position'])
)

chart2 = (points + text + links).properties(title='Firewall State Diagram').interactive()
chart2.save('firewall_state_diagram.json')

# 3. Timeline for a Cyberattack
events = [
    (0, "Attack starts"),
    (5, "Firewall breached"),
    (10, "Data exfiltrated"),
    (15, "Intrusion detected"),
    (20, "Incident response initiated"),
    (30, "Attack contained")
]
timeline_data = pd.DataFrame(events, columns=['time', 'event'])

chart3 = alt.Chart(timeline_data).mark_point().encode(
    x='time:Q',
    y=alt.value(0),
    tooltip=['time:Q', 'event:N']
).properties(title='Cyberattack Timeline').interactive()

chart3.save('cyberattack_timeline.json')