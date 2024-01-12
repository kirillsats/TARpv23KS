from math import *          #был неправильный порядок
import math
a = float(input("Kirjutage külje pikkus=> "))       #Lisasin "float
S = a**2
print(f"Ruudu pindala", round(S,1))
P = a * 4
print("Ruudu ümbermõõt", round(P,1))
di = int(a)*math.sqrt(2)                         #oli "sqr", aga peab olema "sqrt". lisasin "int"algusel
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S = b*c
print("Ristküliku pindala", round(S,2))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di,2))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt"+ str(d))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))