import os 

os.system("cls")

#ENTRADA
num = int(input("Ingresar el número: "))

#PROCESO
seg = num
min = num/60
horas = min / 60
dias = horas / 24

#SALIDA
print("El número en segundos seria: ", int(seg),"segundos")
print("El número en minutos seria: ", int(min),"minutos")
print("El número en horas seria: ", int(horas),"horas")
print("El número en días seria: ", int(dias),"día")