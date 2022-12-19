import os 

os.system("cls")

print ("")
numero = int(input("Ingrese un número: "))

c1 = numero//1000
c2 = (numero%100)//100
c3 = (((numero%1000)%100)//10)
c4 = numero%10

print("El número al revés es", (c4*1000)+(c3*100)+(c2*10)+c1)