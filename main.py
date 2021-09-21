import sys

A=int(input("Podaj a: "))
B=int(input("Podaj b: "))
C=int(input("Podaj c: "))

delta=(B*B)-(4*A*C)

if delta==0:
    x0 = (-B)/(2*A)
    print("Funkcja ma jedno miejsce zerowe: ", x0)
elif delta >0:
    x1 = (-B-(delta))/(2*A)
    x2 = (-B+(delta))/(2*A)
    print("Funkcja ma dwa miejsca zerowe: " ,{x1} ,"i" ,{x2})
else:
    print("Delta mnijesza od zera - brak rozwiązań")
