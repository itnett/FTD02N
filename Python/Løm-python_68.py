python
    class Markedsføring:
        def __init__(self, målgruppe, budskap):
            self.målgruppe = målgruppe
            self.budskap = budskap

        def implementer_strategi(self):
            return f"Markedsføringsstrategi for {self.målgruppe}: {self.budskap}"

    strategi = Markedsføring("Unge voksne", "Bærekraftige produkter")
    print(strategi.implementer_strategi())