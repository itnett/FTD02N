python
class Hund:
    def lag_lyd(self):
        return "Voff!"

class Katt:
    def lag_lyd(self):
        return "Mjau!"

class DyrFabrikk:
    @staticmethod
    def opprett_dyr(dyr_type):
        if dyr_type == "Hund":
            return Hund()
        elif dyr_type == "Katt":
            return Katt()
        else:
            return None

dyr = DyrFabrikk.opprett_dyr("Hund")
print(dyr.lag_lyd())  # Utdata: Voff!