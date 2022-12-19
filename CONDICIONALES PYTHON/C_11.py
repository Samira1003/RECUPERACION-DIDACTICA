import os 

os.system("cls")

print ("Escribe tus ingresos mensuales: ")
ingresos = input ()
ingresos = float (ingresos)

print ("Escribe tus egresos: ")
egresos = input ()
egresos = float(egresos)
efectivo = ingresos - egresos 

if (efectivo<0):
    print("Tienes", efectivo, "Soles y estás en números rojos UnU")
    print("¿Cómo sobrevives XD?")
if (efectivo == 0):
    print("Tienes", efectivo, "Soles, a trabajar OwO")
if (efectivo >0 and efectivo <= 1000):
    print("Tienes", efectivo, "Soles, te va bien uwu")
if (efectivo>1000 and efectivo<10000):
    print("Tienes", efectivo, "Soles, parece que vives en opulencia SIUUUUU")
if (efectivo>10000):
    print("Tienes", efectivo, "Soles, pero compaltan, compaltAn.")