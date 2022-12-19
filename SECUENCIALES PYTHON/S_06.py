import os 

os.system("cls")

#ENTRADA
pi = 3.1416
r = float (input ("Inserte el radio: "))
h = float (input ("Inserte la altura: "))

#PROCESO
Área = 2*pi*r*(r+h)
Volumen = pi*r**2*h

#SALIDA
print ("El área del cilindro es: ", format(Área, ".2f"), "m²")
print ("El volumen es: ", format (Volumen, ".2f"), "m3")