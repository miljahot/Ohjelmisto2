import random
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
        kuljettu = self.atmnopeus * tuntimaara
        uusi_matka = self.kuljettu_matka + kuljettu
        self.kuljettu_matka = uusi_matka


kilpailu = []
for i in range (10):
    auto = Auto("ABC-"+str(i+1), random.randint(100,200))
    kilpailu.append(auto)
    print(f"Auton rekisterinumero: {auto.rekisteritunnus}\nAuton huippunopeus: {auto.huippunopeus} km/h\nAuton tämänhetkinen nopeus:  {auto.atmnopeus}\nAuton kuljettu matka: {auto.kuljettu_matka} ")
    print()



while auto.kuljettu_matka < 10000:
    for auto in kilpailu:
        auto.kiihdyta(random.randint(-10, 15))
        print(f'Auton rekisteritunnus: {auto.rekisteritunnus}\nKuljettu matka: {auto.kuljettu_matka}\n')
        if auto.kuljettu_matka > 10000:
            break
        else:
            auto.kulje(1)

for auto in kilpailu:
    print(f"Auton rekisterinumero: {auto.rekisteritunnus}\nAuton huippunopeus: {auto.huippunopeus} km/h\nAuton tämänhetkinen nopeus:  {auto.atmnopeus}\nAuton kuljettu matka: {auto.kuljettu_matka} ")
    print()