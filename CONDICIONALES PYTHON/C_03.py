import os 

os.system("cls")

n1= int (input ("Ingrese el primer número: "))
n2= int (input("Ingese el segundo número: "))
n3= int (input ("Ingrese el tercer número: "))

if n1 < n2 < n3:
    print("Los números están ordenados de forma creciente")

else:
    print("Los números no están ordenados de forma creciente")