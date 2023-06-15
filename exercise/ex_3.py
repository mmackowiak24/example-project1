class Samochod:
    def __init__(self, marka, model, pojemnosc_silnika, naped, rodzaj_nadwozia, kolor, paliwo):
        self.marka = marka
        self.model = model
        self.pojemnosc_silnika = pojemnosc_silnika
        self.naped = naped
        self.rodzaj_nadwozia = rodzaj_nadwozia
        self.kolor = kolor
        self.paliwo = paliwo

    def __str__(self):
        return self.marka + ' ' + self.model + " " + str(self.pojemnosc_silnika) + " " + self.naped + " " + self.rodzaj_nadwozia + " " + self.kolor + " " + self.paliwo

    def zatankuj(self, iloscPaliwa):
        self.paliwo = self.paliwo + iloscPaliwa
        print("Zatankowano ", iloscPaliwa, " litrów paliwa.")

    def jedz(self):
        spalanie = 0
        if(self.paliwo > 5):
            if(self.pojemnosc_silnika > 3.0):
                spalanie = 10
                self.paliwo = self.paliwo - spalanie
                print("Spalono ", spalanie, " litrów paliwa. W baku pozostało ", self.paliwo, " litrów paliwa.")
            elif(self.pojemnosc_silnika >= 2.0 ):
                spalanie = 8
                self.paliwo = self.paliwo - spalanie
                print("Spalono ", spalanie, " litrów paliwa. W baku pozostało ", self.paliwo, " litrów paliwa.")
            else:
                spalanie = 6
                self.paliwo = self.paliwo - spalanie
                print("Spalono ", spalanie, " litrów paliwa. W baku pozostało ", self.paliwo, " litrów paliwa.")
        else:
            print("halo, halo! proszę zatankować!")


opel_insignia = Samochod("Opel", "Insignia", 2.0, "4x4", "liftback", "czarny", 65)
for i in range(1,10):
    opel_insignia.jedz()
opel_insignia.zatankuj(25)
opel_insignia.jedz()
