figura = input("Que es un circulo o triangulo: ")
if(figura == "triangulo"):
    base = int(input("Que base tiene: "))
    altura = int(input("Que altura tiene: "))
    area_triangulo = (base*altura)/2
    print("El area del triangulo es igual a: ",area_triangulo)
else:
    if(figura == "circulo"):
        radio = int(input("Que radio tiene: "))
        area_circulo = (radio*radio*3.141592)
        print("El area del circulo es: ",area_circulo)
