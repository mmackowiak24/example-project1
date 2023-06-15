# trojkat
import math

a = 10
b = 20
c = 15
h = 12
r = 5

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")


# prostokat

obwod = a + b + a + b
pole = a * b
print("Obwod prostokata wynosi "+ str(obwod) + ", zas pole wynosi " + str(pole) + ".")


#kwadrat
obwod = 4*a
pole = a*a
print("Obwod kwadratu wynosi "+ str(obwod) + ", zas pole wynosi " + str(pole) + ".")

#kolo
obwod = 2 * math.pi * r
pole = math.pi * pow(r,2)
print("Obwod koła wynosi "+ str(obwod) + ", zas pole wynosi " + str(pole) + ".")

#trapez
obwod = a + b + c + d
pole = ((a + b) * h) / 2
print("Obwod trapeza wynosi "+ str(obwod) + ", zas pole wynosi " + str(pole) + ".")



