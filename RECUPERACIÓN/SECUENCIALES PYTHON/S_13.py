import os 

os.system("cls")

#ENTRADA
juan = float(input("Dolares aportados Juan: "))
rosa = float(input("Dolares aportados Rosa: "))
daniel = float(input("Soles aportados Daniel: "))

#PROCESO
capdolar = juan + rosa + (daniel/3)
juanporc = (juan*100)/capdolar
rosaporc = (rosa*100)/capdolar
danielporc = ((daniel/3)*100)/capdolar

#SALIDA
print("El capital en dolares es: ", format(capdolar,".2f"))
print("El porcentaje en dolares de Juan es: ", format(juanporc,".2f")+ " %")
print("El porcentaje en dolares de Rosa es: ", format(rosaporc,".2f")+ " %")
print("El porcentaje en dolares de Daniel es: ", format(danielporc,".2f")+ " %")