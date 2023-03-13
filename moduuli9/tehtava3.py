class Auto:
    def __init__(self,rekisteritunnus, huippunopeus, atmnopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.atmnopeus = atmnopeus
        self.kuljettu_matka = kuljettumatka

    def kiihdyta(self,muutos):
        if self.atmnopeus + muutos >= self.huippunopeus:
            self.atmnopeus =self.huippunopeus
        elif self.atmnopeus + muutos <0:
            self.atmnopeus = 0
        else:
            self.atmnopeus += muutos

    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.atmnopeus * tuntimaara
        return self.kuljettu_matka


auto = Auto('ABC-123', 142)
print(f"Auton rekisterinumero: {auto.rekisteritunnus}\nAuton huippunopeus: {auto.huippunopeus} km/h\nAuton tämänhetkinen nopeus:  {auto.atmnopeus}\nAuton kuljettu matka: {auto.kuljettu_matka} ")

auto.kiihdyta(30)

print(f'\nAuton tämänhetkinen nopeus: {auto.atmnopeus}')
auto.kulje(1.5)
print(f'Kuljettu matka: {auto.kuljettu_matka} km')
