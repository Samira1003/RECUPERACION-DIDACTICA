import os 

os.system("cls")

#ENTRADA
ht = int(input("Horas trabajadas: "))
th = int(input("Tarifa horaria: "))

#PROCESO
sb = ht * th
bonif = (sb*20)/100
sbr= sb + bonif
dcto = (sbr * 10) /100
sneto = sbr - dcto

#SALIDA
print("El sueldo básico sería: ", format(sb,".2f"))
print("El sueldo bruto sería: ", format(sbr,".2f"))
print("El sueldo neto sería: ", format(sneto,".2f"))