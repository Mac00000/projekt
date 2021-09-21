""""
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
"""

import sys
import math
print(sys.argv)

A=int(sys.argv[1])
B=int(sys.argv[2])
C=int(sys.argv[3])

delta=math.pow(B,2)-(4*A*C)

if(delta < 0):
    print("Nie ma miejsc zerowych")
elif(delta==0):
    x1=-B/(2*A)
    print(f"Funkcja zawiera 1 miejsce zerowe: {x1}")
else:
    x1=(-B-math.sqrt(delta))/(2*A)
    x2=(-B+math.sqrt(delta))/(2*A)
    print(f"Funkcja zawiera 2 miejsca zerowe: {x1} oraz {x2}")
