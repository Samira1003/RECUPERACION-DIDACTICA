import os 

os.system("cls")

#Entrada
varones = int(input("varones: "))
mujeres = int(input("mujeres: "))

#Proceso
total = varones + mujeres
pv = varones * 100/ total
pm = mujeres * 100/ total

#Salida
print("% de varones es: ",format(pv,".2f") + " %")
print("% de mujeres es: ",format(pm,".2f") + " %")