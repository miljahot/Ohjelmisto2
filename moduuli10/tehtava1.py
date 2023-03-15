class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.akerros = alin_kerros
        self.ykerros = ylin_kerros
        self.atmkerros = alin_kerros

    def siirry_kerrokseen(self,kerros):
        while self.atmkerros < kerros:
            if kerros > self.ykerros:
                kerros = self.ykerros
            self.kerros_ylos()
        while self.atmkerros > kerros:
            if kerros < self.akerros:
                kerros = self.akerros
            self.kerros_alas()

    def kerros_ylos(self):
        self.atmkerros +=1
        print(f'Olet kerroksessa: {self.atmkerros}')
    def kerros_alas(self):
        self.atmkerros -=1
        print(f'Olet kerroksessa: {self.atmkerros}')



h =Hissi(0,10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)