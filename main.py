class Hayvon:
    def __init__(self, turi, ovoz):
        self.turi = turi
        self.ovoz = ovoz

    def ovoz_chiqar(self):
        print(f"{self.turi} ovozi: {self.ovoz}")


class Kuchuk(Hayvon):
    def __init__(self):
        super().__init__("Kuchuk", "Vov-vov")


class Mushuk(Hayvon):
    def __init__(self):
        super().__init__("Mushuk", "Miyov-miyov")


kuchuk = Kuchuk()
mushuk = Mushuk()

kuchuk.ovoz_chiqar()
mushuk.ovoz_chiqar()
