class Auto:
    def __init__(self,rekisteritunnus, huippunopeus, atmnopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.atmnopeus = atmnopeus
        self.kuljettumatka = kuljettumatka



auto = Auto('ABC-123', 142)
print(f"Auton rekisterinumero: {auto.rekisteritunnus}\nAuton huippunopeus: {auto.huippunopeus} km/h\nAuton tämänhetkinen nopeus:  {auto.atmnopeus}\nAuton kuljettu matka: {auto.kuljettumatka} ")
