
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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus,huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class PolttomoottoriAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = tankin_koko


sahkoauto = Sahkoauto('ABC-15', 180, 52.5)
moottoriauto = PolttomoottoriAuto('ACD-123', 165, 32.2)
print(f'Sähköauton kuljettu matka: {sahkoauto.kuljettu_matka}')
print(f'Polttomoottoriauton kuljettu matka: {moottoriauto.kuljettu_matka}\n')
sahkoauto.kiihdyta(50)
moottoriauto.kiihdyta(30)

sahkoauto.kulje(3)
moottoriauto.kulje(3)


print(f'Sähköauton kuljettu matka 3 tunnin jälkeen: {sahkoauto.kuljettu_matka}')
print(f'Polttomoottoriauton kuljettu matka 3 tunnin jälkeen: {moottoriauto.kuljettu_matka}')