import os 

os.system("cls")

#Compra < $800 -> Descuento 0%
# $800  <- Compra <- $1500 -> Descuento 10% 
# $1500  <- Compra <- $5000 -> Descuento 15%
# $5000 <- Compra -> Descuento 20%

compra = float (input("Ingrese el monto de la compra: "))

if compra < 800:
    print ("Eñ total a pagar es: ", compra)
elif 800 <= compra <= 1500:
    compra -= (compra * 0.10)
    print ("El total a pagar, con su respectivo descuento, es: ", compra)
elif 1500 < compra <= 5000:
    compra -= (compra * 0.15)
    print ("El total a pagar, son su respectivo descuento, es: ", compra)
else:
    compra -= (compra * 0.20)
    print ("El total a pagar, con su respectivo descuento, es: ", compra)