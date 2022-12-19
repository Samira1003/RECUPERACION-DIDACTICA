import os 

os.system("cls")

print ("Ingrese el nombre del empleado: ")
nombre=input()
print ("Cuánas hotas trabajo esta semana", nombre, ":")

horas = input ()
horas = int (horas)
print ("¿Cuánto se paga por hora?: ")

precioH = input()
precioH =float (precioH)

if (horas<=40):
    pago = horas*precioH
    print("El sueldo final de", nombre, "Es $", pago)

else:
    extras = horas - 40
    pago = 40 * precioH
    pagoFinal = pago + (extras*precioH*2)
    print("El sueldo final de", nombre, "Es $", pagoFinal)