from asyncore import write
import csv
pracownicy = [] #zaciagane z csv


class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
    
    def __str__(self):
        pass

    def oblicz_netto(self):
        ubezpieczenie_emerytalne = wynagrodzenie_brutto * 0.098
        ubezpieczenie_rentalne = wynagrodzenie_brutto * 0.015
        ubezpieczenie_chorobowe = wynagrodzenie_brutto * 0.024
        ubezpieczenie_zdrowotne = wynagrodzenie_brutto * 0.078
        zaliczka_podatek = wynagrodzenie_brutto * 0.03
        wynagrodzenie_netto = wynagrodzenie_brutto - (ubezpieczenie_emerytalne + ubezpieczenie_rentalne + ubezpieczenie_chorobowe + ubezpieczenie_zdrowotne + zaliczka_podatek)

        print("Ubezpieczenie emerytalne: ", ubezpieczenie_emerytalne)
        print("Ubezpieczenie rentalne: ", ubezpieczenie_rentalne)
        print("Ubezpieczenie chorobowe: ", ubezpieczenie_chorobowe)
        print("Ubezpieczenie zdrowotne: ", ubezpieczenie_zdrowotne)
        print("Zaliczka na podatek:", zaliczka_podatek)
        print("Wynagrodzenie brutto - netto:", wynagrodzenie_brutto, " - ", wynagrodzenie_netto, "=", wynagrodzenie_brutto - wynagrodzenie_netto)


    def oblicz_koszty(self):
        return 0


    def wypisz_pracownika(self):
        print(imie, nazwisko, wynagrodzenie_brutto)

    print("Suma kosztów wynosi: xxx")


with open('salary.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader,None)
    for imie, nazwisko, wynagrodzenie_brutto in reader:
            wynagrodzenie_brutto = float(wynagrodzenie_brutto)
            pracownicy.append(Pracownik(imie, nazwisko, wynagrodzenie_brutto))


for c,i in enumerate(pracownicy):
    print("index is", c)
    print("Imie:", i.imie," - ", "Nazwisko: ", i.nazwisko, " - ","Wynagrodzenie brutto: ", i.wynagrodzenie_brutto)
    i.oblicz_netto()
    #c.oblicz_koszty()
