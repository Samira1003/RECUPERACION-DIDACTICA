import os 

os.system("cls")

numero=input("Ingrese un número de 4 dígitos: ")

if int(numero [0]) % 2 == 0:
    if int(numero [1]) %2 == 0:
        if int (numero [2]) % 2 == 0:
            if int (numero [3]) % 2 == 0:
                print("Todos los dígitos son pares.")
            else:
                print("No todos los dígitos son pares.")
        else:
            print("No todos los dígitos son pares.")
    else:
        print("No todos los dígitos son pares.")
else:
    print("No todos los dígitos son pares.")
