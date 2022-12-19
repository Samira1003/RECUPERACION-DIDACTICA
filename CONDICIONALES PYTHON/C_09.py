import os 

os.system("cls")

import math


a=float(input("Ingrese el primer lado del triángulo: "))
b=float(input("Ingrese el segundo lado del triángulo: "))
c=float(input("Ingrese el tercer lado del triángulo: "))

#a+b>c
#a+c>b
#b+c>a

if (a+b)>c and (a+c)>b and (b+c)>a:
    print("\nLos lados corresponde a un triángulo.")

    s=(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("El área del triángulo es", area)

#Equilátero = Todos los lados iguales = a=b a=c
#Isósceles = 2 lados iguales = a=b o a=c o b=c
#Escaleno = No tiene lados iguales

    if (a==b==c):
        print("Se trata de un triángulo equilátero.")
    elif (a==b or a==c or b==c):
        print("Se trata de un triángulo esósceles.")
    else:
        print("Se trata de un triángulo escaleno.")

else:
    print("\nLos lados no corresponde a un triángulo.")

