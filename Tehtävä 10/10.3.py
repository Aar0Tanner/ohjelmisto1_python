class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
        return print(f"hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
        return print(f"hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print("Virhe: kerros on sallitun alueen ulkopuolella.")
            return

        while self.kerros < kohde:
            self.kerros_ylos()

        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alinnro, ylinnro, hissilkm):
        self.alinnro = alinnro
        self.ylinnro = ylinnro
        self.hissit = []

        for i in range(hissilkm):
            uusi_hissi = Hissi(alinnro, ylinnro)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, hissinro, kohde):
        if 0 <= hissinro < len(self.hissit):
            self.hissit[hissinro].siirry_kerrokseen(kohde)
        else:
            print(f"Hissiä numero {hissinro} ei ole olemassa.")
        return

    def palohalytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alinnro)


t = Talo(1, 10, 3)

t.aja_hissia(0, 5)
t.aja_hissia(1, 8)
t.aja_hissia(2, 3)

t.palohalytys()
