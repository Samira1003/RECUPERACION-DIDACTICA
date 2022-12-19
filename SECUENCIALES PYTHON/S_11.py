import os 

os.system("cls")

#ENTRADA
num1 = int (input("Ingresar el primer número: "))
num2 = int(input ("Ingresar el segundo número: "))

#PROCESO
n1 = int(num1/100)
n2= int((num1%100)/10)
n3= num1 % 10

n4= int(num2/100)
n5= int ((num2%100)/10)
n6= num2 % 10

#SALIDA
print("Rpta :{}{}{}". format(n6,n2,n4))
print("Rpta :{}{}{}". format(n3,n5,n1))