import os 

os.system("cls")

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if n1 % n2 == 0:
    print (n2, "Es divisor de", n1)
else:
    print (n2, "No es divisor de", n1)