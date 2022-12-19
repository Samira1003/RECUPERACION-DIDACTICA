import os 

os.system("cls")

age = input ("Ingrese su edad: ")
age = int(age)

if (age > 0) and (age < 130):
    if age >= 18:
        print("Es mayor de edad: ")
    else:
        print("No es mayor de edad")
else:
    print("Ingrese una edad correcta")