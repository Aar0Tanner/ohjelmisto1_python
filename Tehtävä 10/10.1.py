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


h = Hissi(1, 10)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(h.alin)