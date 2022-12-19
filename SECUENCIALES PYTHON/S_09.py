import os 

os.system("cls")

#ENTRADA
num = int(input("Ingresa número: "))

#PROCESO
n1= int (num / 1000)
n2= int ((num % 1000) / 100)
n3= int (((num%1000)%1000) /10)
n4= num % 10

suma = n1 + n2 + n3 + n4

#SALIDA
print("La suma es: ", format(suma,".2f"))

