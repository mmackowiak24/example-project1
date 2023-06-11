#1 - find_max
#wez liste -> sprawdz pierwszy obiekt -> wpisz go na zmienną jako maksymalną wartość -> wywołaj funkcję dla kolejnego obiektu jeśli lista nie jest pusta -> sprawdź czy liczba jest większa niż poprzednia:
# tak - nadpisz zmienną
# nie - nie nadpisuj zmiennej
# sprawdź czy jest kolejny element na liście
# tak - wywołaj funkcje i powtórz powyższe kroki
# nie - koniec programu
import numpy as numpy

liczby = [1,3,5,8]

def find_max(numbers):
    maxNumber = 0
    if(numbers[0] > maxNumber):
        maxNumber = numbers[0]
        numbers.pop(0)
        if( len(numbers) >= 1):
            return find_max(numbers)
        else:
            return maxNumber
a = find_max(liczby)
print("find max:", a)

#2 - sum_of_list
# wez liste -> wez pierwszy element i wpisz go na sume -> sprawdz czy lista ma kolejne elementy:
# tak: usuń element o indeksie 0 i wywołaj funkcje ponownie
# nie: koniec funkcji
liczby = [1,3,5,8]

def sum_of_list(numbers):
    sum_of_elements = 0 + numbers[0]
    numbers.pop(0)
    if(len(numbers) > 0):
        return (sum_of_elements + sum_of_list(numbers))
    else:
        return sum_of_elements

b = sum_of_list(liczby)
print("sum of list:", b)

#3 - n!
#jeśli liczba jest mniejsza bądź równa 1: return 1
#w przeciwnym wypadku: return liczba * silnia(liczba-1)
liczba = 5
def silnia(number):
    if(number <= 1):
        mySilnia = number
        return mySilnia
    else:
        mySilnia = number
        return (mySilnia * silnia(number - 1))

c = silnia(liczba)
print("silnia:", c)


#4 Ciag fibonacciego - użytkownik podaje liczbe, według której generowane są kolejne elementy ciągu fibonacciego (input 5 - 5 elementów ciągu)
#fibonacci:
#0 dla n = 0
#1 dla n = 1
#fibonacci(n-1) + fibonacci(n-2) dla n>1
liczba = 10
def fibonacci(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))

print(fibonacci(liczba))


#5 Sudoku - program iteruje po kolumnach i sprawdza czy są puste.
# puste: sprawdź od numeru 1-4 który pasuje i go wprowadź
# rozwiąż sudoku dla wprowadzonej liczby
# jeśli się nie da: zmień na 0 i sprawdź inne cyfry

sudoku = [[1,0,0,0],
          [0,0,0,4],
          [0,0,2,0],
          [0,3,0,0]]
#sprawdź czy można wstawić liczbę
def isPossible(matrix, row, column, n):
    #wiersze
    for i in range(0, 4):
        if matrix[row][column] == n:
            return False
    #kolumny
    for i in range(0, 4):
        if matrix[i][column] == n:
            return False

    #macierz 2x2
    row0 = (row // 2) * 2
    col0 = (column // 2) * 2
    for i in range(2):
        for j in range(2):
            if matrix[row0 + i][col0 + j] == n:
                return False
    return True

def solve_sudoku(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                for n in range(1, 5):
                    if isPossible(matrix, i, j, n):
                        matrix[i][j] = n
                        solve_sudoku(matrix)
                        matrix[i][j] = 0
                return None
    print(numpy.matrix(matrix))

solve_sudoku(sudoku)

