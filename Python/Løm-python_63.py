python
    class Likviditet:
        def __init__(self, omløpsmidler, kortsiktig_gjeld):
            self.omløpsmidler = omløpsmidler
            self.kortsiktig_gjeld = kortsiktig_gjeld

        def beregn_likviditet(self):
            return self.omløpsmidler / self.kortsiktig_gjeld

    likviditet = Likviditet(200000, 100000)
    print(f"Likviditetsgrad: {likviditet.beregn_likviditet()}")