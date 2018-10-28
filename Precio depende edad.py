edad = 0;
precioFinal = 0;

edad = int(input("Introduce tu edad: "))

if edad <5:
    precioFinal = 0;

if edad >=65:
    precioFinal = 0;

if edad >5 and edad <65:
    precioFinal = 2.15;

print("El precio final es:",precioFinal);
