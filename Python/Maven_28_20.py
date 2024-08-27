python
    import plotly.express as px

    data = {
        "Kvartal": ["Q1", "Q2", "Q3", "Q4"],
        "Inntekt": [10000, 15000, 12000, 18000]
    }

    fig = px.bar(data, x="Kvartal", y="Inntekt", title="Kvartalsvis Inntekt")
    fig.show()