import os 

os.system("cls")

#entrada
metros = float(input ("Ingresar los metros deseados:"))

#Proceso
centimetros = metros * 100
pulgadas = centimetros / 2.54
pie = pulgadas/12
yardas = pie/3

#Salidas
print("En centímetros: ", format (centimetros, ".2f"))
print("En pulgadas: ", format (pulgadas, ".2f"))
print("En pie: ", format (pie, ".2f"))
print("En yardas: ", format (yardas, ".2f"))
