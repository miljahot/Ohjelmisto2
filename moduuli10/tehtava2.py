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

class Talo:
    def __init__(self,alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissit = []
        for i in range(self.hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissia(self,hissi_nro, kohde):
        print(f'Ajetaan hissiä: {hissi_nro} kerrokseen {kohde}')
        self.hissit[hissi_nro-1].siirry_kerrokseen(kohde)


koti =Talo(1,6,3)
koti.aja_hissia(1,5)
print()
koti.aja_hissia(3,4)