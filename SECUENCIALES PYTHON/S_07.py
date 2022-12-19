import os 

os.system("cls")

#ENTRADA
base = float (input("Insertar la base: "))
altura = float (input ("Insertar la altura: "))

#PROCESO
area = base * altura
perimetro = 2*(altura + base)

#SALIDA
print ("El área del rectángulo es: ", format(area,".2f"), "m²")
print ("El perimetro es: ", format(perimetro,".2f"), "m")