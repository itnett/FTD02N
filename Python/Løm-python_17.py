python
class DirekteKostnader:
    def __init__(self, materialkostnader, lønnskostnader):
        self.materialkostnader = materialkostnader
        self.lønnskostnader = lønnskostnader

    def totale_direkte_kostnader(self):
        return self.materialkostnader + self.lønnskostnader

direkte_kostnader = DirekteKostnader(20000, 15000)
print(f"Totale Direkte Kostnader: {direkte_kostnader.totale_direkte_kostnader()}")