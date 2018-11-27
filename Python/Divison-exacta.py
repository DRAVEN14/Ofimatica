#coding utf-8
dividendo = int(input("Escribe un dividendo: "))
divisor = int(input("Escribe un divisor: "))
if(divisor==0):
    print("No se puede divir por 0")
cociente = (dividendo/divisor)
residuo = (dividendo%divisor)
if(residuo!=0):
    print("La division no es exacta. Cociente: ",cociente,"Residuo: ",residuo)
else:
    print("La divison es exacta. Cociente: ",cociente)
