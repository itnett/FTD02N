python
class Elbil(Bil):
    def lad(self):
        print("Lader batteriet...")

min_elbil = Elbil("Nissan Leaf")
min_elbil.kjør()
min_elbil.lad()