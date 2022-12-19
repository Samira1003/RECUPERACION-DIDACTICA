import os 

os.system("cls")

#ENTRADA
num = int (input("Ingresa número: "))

#PROCESO
n1 = int(num/1000) 
n2 = int ((num % 1000) / 100)
n3 = int (((num % 1000)%100)/10)
n4 = num % 10

#SALIDA
print("Respuesta : {}{}{}{}". format(n4,n3,n2,n1))
