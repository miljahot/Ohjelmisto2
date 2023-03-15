import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, atmnopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.atmnopeus = atmnopeus
        self.kuljettu_matka = kuljettumatka

    def kiihdyta(self, muutos):
        if self.atmnopeus + muutos >= self.huippunopeus:
            self.atmnopeus = self.huippunopeus
        elif self.atmnopeus + muutos < 0:
            self.atmnopeus = 0
        else:
            self.atmnopeus += muutos

    def kulje(self, tuntimaara):
        kuljettu = self.atmnopeus * tuntimaara
        uusi_matka = self.kuljettu_matka + kuljettu
        self.kuljettu_matka = uusi_matka


class Kilpailu:
    def __init__(self, nimi, pituus, lkm):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []
        self.aika =0

        for i in range(lkm):
            auto = Auto("ABC-" + str(i + 1), random.randint(100, 200))
            self.autot.append(auto)
        while not self.kilpailu_ohi():
            self.tunti_kuluu()
            self.tulosta_tilanne()

    def tunti_kuluu(self):
        self.aika += 1
        #print('Tunti')
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

            # print(f'Auton rekisteritunnus: {auto.rekisteritunnus}\nKuljettu matka: {auto.kuljettu_matka}\n')

    def tulosta_tilanne(self):

        if(self.aika % 10 == 0 or self.kilpailu_ohi()):
            print(f'Aika: {self.aika}h')
            print('Tilanne:')
            for auto in self.autot:
                print(f"Auton rekisterinumero: {auto.rekisteritunnus} Auton huippunopeus: {auto.huippunopeus} km/h Auton tämänhetkinen nopeus:  {auto.atmnopeus} Auton kuljettu matka: {auto.kuljettu_matka} ")


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka > self.pituus:
                return True


'''print(f"Auton rekisterinumero: {auto.rekisteritunnus}\nAuton huippunopeus: {auto.huippunopeus} km/h\nAuton tämänhetkinen nopeus:  {auto.atmnopeus}\nAuton kuljettu matka: {auto.kuljettu_matka} ")
print()'''

ralli = Kilpailu('Suuri romuralli', 8000, 10)
