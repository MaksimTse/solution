from math import * #perepisal import naoborot 

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #dobavil format
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) #math ne nuzhen
print("Ruudu diagonaal", round(di,2)) #izmenil okruglenie
print()
print("Ristküliku karakteristikud") #ubral skobku
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #dobavil format
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #dobavil format
S=b*c
print("Ristküliku pindala", S) #dobavil kovichki
P=2*(b+c) #ispravil formulu
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #ispravil formulu, math ne nuzhen
print("Ristküliku diagonaal", round(di,2)) #dobavil okruglenie
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #izmenil format
d=2*r
print("Ringi läbimõõt", d)
S=pi*r**2 #ispravil formulu
print("Ringi pindala", round(S,2)) #dobavil okruglenie
C=2*pi*r
print("Ringjoone pikkus", round(C,2)) #dobavil okruglenie
