# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello,student))


# zadanie 1.2

# student = input("Wpisz swoje imie: ")
# print("Hello "+student)


# zadanie 1.3 - policz liczbe studentow w tablicy studenci 
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: ", liczba_studentow)


# zadanie 1.4 - za pomoca petli i print przywitaj sie z kazdym studentem z tabeli studenci osobno
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
for x in range(liczba_studentow):
    print(studenci[x])


# zadanie 1.5
liczba = 3
potega = 4
wynik = pow(liczba,potega)

# Wynik wynosi: 81
print("Wynik wynosi: ",wynik)


# zadanie 1.6
# policz ilosc nawiasow ( w danym ciagu znakow
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))


# zadanie 1.7
# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)


# zadanie 1.8
# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda name: name.split(" ")[-1].lower())
# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)


# zadanie 1.9
# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studentN = 0
for student in studenci:
    if student.split(" ")[-1].lower().startswith("n"):
        studentN += 1
print("Liczba studentow na N wynosi: ",studentN)


# zadanie 1.10
# zmienne poniezej preprezentuja ulozenie punktow na wykresie
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def isLinear(coordinates):
    if len(coordinates) < 3:
        return True #z dwóch punktów można utworzyć funkcję liniową
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    slope = (y2 - y1 ) / (x2 - x1) if x2 != x1 else float('inf')

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        new_slope = (y - y1) / (x - x1) if x != x1 else float('inf')
        if abs(new_slope - slope ) >= 1e-9:
            return False
    return True
# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

print(isLinear(wykres_1))
print(isLinear(wykres_2))
print(isLinear(wykres_3))