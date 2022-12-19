import os 

os.system("cls")

opcion_medidas= int (input("***MENÚ PRINCIPAL***\n1.MEDIDAS DE LONGITUD\n2. MEDIDAS DE VOLUMEN"
"\n3.MEDIDAS DE PESO\nEscoja la opción que desea: "))

if opcion_medidas == 1:
    print ("\n***MEDIDAS DE LONGITUD***\n")
    opcion_submenu = int(input("1.Pulgadas a milímetros \n2. Yardas a metros \nEscoja la opción que desea: "))

    if opcion_submenu == 1:
        print ("-------------------------")
        pulgadas = int(input("Ingrese la cantidad de pulgadas a converir: "))
        milimetros = pulgadas * 25.40
        print(pulgadas, "pulgadas equivales a", milimetros, "milímetros")
    
    elif opcion_submenu == 2:
        print ("-------------------------")
        yardas = int(input("Ingrese la cantidad de yardas a convertir: "))
        metros = yardas * 0.9144
        print (yardas, "yardas equivales a", metros, "metros")
    
    else:
        print("La opción escogida no es válida.")