import os 

os.system("cls")

opcion = int (input("***menú*** \n1. Pulgadas a milímetros \n2. Yardas a metros \n3. Millas a kilómetros \n"
"Ingrese la opción que desea: "))

if opcion == 1:
    print ("--------------------------")
    pulgadas= int(input("Ingrese la cantidad de pulgadas a convertir: "))
    milimetros = pulgadas * 25.40
    print (pulgadas, "pulgadas equivalen a", milimetros, "milímetros")
elif opcion == 2:
    print ("--------------------------")
    yardas = int (input("Ingrese la cantidad de yardas a convertir: "))
    metros = yardas * 0.9144
    print (yardas, "yardas equivalen a", metros, "metros")
elif opcion == 3:
    print ("--------------------------")
    millas = int (input("Ingerse la cantidad de millas a convertir: "))
    kilometros = millas * 1.6093
    print(millas, "millas equivalen a", kilometros, "kilómetros")
else:
    print("Ingrese una opción válida.")
