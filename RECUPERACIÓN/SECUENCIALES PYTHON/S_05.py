import os 

os.system("cls")

#Entrada
giga = int(input("Ingrese los gigabytes: "))

#Proceso
megas = giga * 1024
kylo = megas * 1024
byte = kylo * 1024

#Salida
print("La cantidad de megabytes sería: ", format(megas, ".2f"), "MB")
print("La cantidad de kilobytes sería: ", format(kylo, ".2f"), "KB")
print("La cantidad de bytes sería: ", format(byte, ".2f"), "B")