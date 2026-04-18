class Chegirma:
    def __init__(self, asosiy_narx, promo_kod):
        self.asosiy_narx = asosiy_narx
        self.promo_kod = promo_kod

    def asosiy_chegirma(self):
        return self.asosiy_narx * 0.1

    def promo_chegirma(self):
        if self.promo_kod == "PROMO10":
            return self.asosiy_narx * 0.1
        elif self.promo_kod == "PROMO20":
            return self.asosiy_narx * 0.2
        else:
            return 0

    def umumiy_chegirma(self):
        return self.asosiy_chegirma() + self.promo_chegirma()

    def yangi_narx(self):
        return self.asosiy_narx - self.umumiy_chegirma()

asosiy_narx = 100
promo_kod = "PROMO10"
chegirma = Chegirma(asosiy_narx, promo_kod)
print(f"Asosiy chegirma: {chegirma.asosiy_chegirma()}")
print(f"Promo chegirma: {chegirma.promo_chegirma()}")
print(f"Umumiy chegirma: {chegirma.umumiy_chegirma()}")
print(f"Yangi narx: {chegirma.yangi_narx()}")
