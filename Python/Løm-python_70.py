python
    class Markedsplan:
        def __init__(self, mål, strategier, tiltak):
            self.mål = mål
            self.strategier = strategier
            self.tiltak = tiltak

        def vis_plan(self):
            return f"Mål: {self.mål}, Strategier: {self.strategier}, Tiltak: {self.tiltak}"

    plan = Markedsplan("Øke salg med 20%", ["Digital markedsføring", "Rabattkampanjer"], ["Sosiale medier annonsering", "Nyhetsbrev"])
    print(plan.vis_plan())