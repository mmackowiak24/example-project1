from asyncore import write
import csv
pracownicy = [] #zaciagane z csv


class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.ubezpieczenie_emerytalne = wynagrodzenie_brutto * 0.0976
        self.ubezpieczenie_rentalne = wynagrodzenie_brutto * 0.015
        self.ubezpieczenie_chorobowe = wynagrodzenie_brutto * 0.0245
        self.ubezpieczenie_zdrowotne = wynagrodzenie_brutto * 0.09
    
    def __str__(self):
        pass

    def oblicz_netto(self):
        zaliczka_podatek = self.wynagrodzenie_brutto * 0.03
        wynagrodzenie_netto = self.wynagrodzenie_brutto - (self.ubezpieczenie_emerytalne + self.ubezpieczenie_rentalne + self.ubezpieczenie_chorobowe + self.ubezpieczenie_zdrowotne + zaliczka_podatek)
        kwota_brutto = self.wynagrodzenie_brutto - wynagrodzenie_netto
        print("WYNAGRODZENIE BRUTTO")
        print("Wynagrodzenie brutto wynosi: ", self.wynagrodzenie_brutto, "\n")
        print("WYNAGRODZENIE NETTO")
        print("Ubezpieczenie emerytalne: ", round(self.ubezpieczenie_emerytalne))
        print("Ubezpieczenie rentalne: ", round(self.ubezpieczenie_rentalne))
        print("Ubezpieczenie chorobowe: ", round(self.ubezpieczenie_chorobowe))
        print("Ubezpieczenie zdrowotne: ", round(self.ubezpieczenie_zdrowotne))
        print("Zaliczka na podatek:", round(zaliczka_podatek))
        print("Wynagrodzenie brutto - netto:", round(self.wynagrodzenie_brutto), " - ", round(kwota_brutto), "=", round(wynagrodzenie_netto))
        return wynagrodzenie_netto


    def oblicz_koszty(self):
        print("KOSZTY PRACODAWCY")
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        skladka_rentowa = self.wynagrodzenie_brutto * 0.065
        skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0067
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        fundusz_gwar_swiad_pracowniczych = self.wynagrodzenie_brutto * 0.001
        koszt_pracodawcy = self.wynagrodzenie_brutto + (skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + fundusz_pracy + fundusz_gwar_swiad_pracowniczych)
        print("Całkowity koszt pracodawcy wynosi: ", koszt_pracodawcy)
        return koszt_pracodawcy


    def wypisz_pracownika(self):
        print(imie, nazwisko, wynagrodzenie_brutto)
    print("Suma kosztów wynosi: xxx")


with open('salary.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for imie, nazwisko, wynagrodzenie_brutto in reader:
        wynagrodzenie_brutto = float(wynagrodzenie_brutto)
        pracownicy.append(Pracownik(imie, nazwisko, wynagrodzenie_brutto))


for c, i in enumerate(pracownicy):
    print("\n")
    print(c, "- Imie:", i.imie, " - ", "Nazwisko: ", i.nazwisko, " - ", "Wynagrodzenie brutto: ", i.wynagrodzenie_brutto)
    i.oblicz_netto()
    print("\n")
    i.oblicz_koszty()
