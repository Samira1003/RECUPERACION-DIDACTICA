import os 

os.system("cls")

tienes_llave = input ("¿Tienes la llave?")

if tienes_llave=="si":
    forma= input ("¿Qué forma tiene la llave?")
    color = input ("¿Qué color tiene la llave?")
    if forma == "Cuadrada" and color == "Naranja":
        print ("Entra por la puerta 1.")
    elif forma == "redonda" and color == "Amarillo":
        print ("Entra por la puerta 2.")
    elif forma == "triangular" and color == "Rojo":
        print("Entra por la puerta 3.")
    else:
        print("Tienes la llave equivocada")

else:
    print("No puede pasar")

print("Fin")