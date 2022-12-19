import os 

os.system("cls")

#ENTRADA
tramo1K = float(input("Ingresar el tramo 1 en kilometros: "))
tramo2P = float(input("Ingresar el tramo 2 en pies: "))
tramo3M = float(input("Ingresar el tramo 3 en millas: "))

#PROCESO
metro1 = tramo1K * 1000
metro2 = tramo2P / 3.2808
metro3 = tramo3M * 1600

totalmetros = metro1 + metro2 + metro3
totalyardas = totalmetros * 0.914


#SALIDA
print("total recorrido en metros seria: ", format(totalmetros,".2f"))
print("total recorrido en yardas seria: ", format(totalyardas,".2f"))