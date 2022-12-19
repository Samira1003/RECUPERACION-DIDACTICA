import os 

os.system("cls")

#Entrada
pies = int(input("pies: "))
pulgadas = int(input("pulgadas: "))

#Proceso
metros = (pies * 12 + pulgadas) * 2.54/100

#Salida
print("metros =", format(metros,"2f")), "m"
print ("")