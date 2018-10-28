edad = 0;
sexe = 1;          #0 és dona, 1 és home
colorCabell = 0;
precioFinal = 0;

edad = int(input("Introduce tu edad: "))
sexe = input("Introduce tu genero (M si eres mujer, H si eres hombre): ")
colorCabell = int(input("Cual es el color de tu pelo? (1 Rubio/a, 2 Peliroja, 3 Morena, 0 para otro): "))
jubilat = input("Estas jubilado? (si, no): ")

if sexe == "H":
    if jubilat == "no":
        precioFinal == 1;

if sexe == "M":
    if jubilat == "no" and colorCabell == 1: 
        precioFinal = 0;

if sexe == "H, M":
    if jubilat == "si" and edad > 65:
        precioFinal = 0;

if sexe == "M":
    if jubilat == "no" and colorCabell == 0:
        precioFinal = 0.5;

        print("El precio final es:",precioFinal);

