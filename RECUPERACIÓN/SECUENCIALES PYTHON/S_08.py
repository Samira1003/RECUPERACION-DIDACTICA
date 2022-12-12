import os 

os.system("cls")

#ENTRADA
pi = 3.1416
r = float(input("Inserte medida del radio: "))
h = float(input("Insertar la altura: "))

#PROCESO
ab = pi*r**2
al = 2*pi*r*h
at = (2*ab) + al

#SALIDA
print ("El área de la base es: ", format(ab,".2f"), "m²")
print ("El área lateral es: ", format(al,".2f"), "m²")
print ("El área total es: ", format(at,".2f"), "m²")