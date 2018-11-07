#coding:uft8
anyo_actual = int(input("En que anyo estamos: "))
anyo_cualquiera = int(input("Pon un anyo cualquiera: "))
resultado = abs(anyo_actual-anyo_cualquiera)

if(anyo_actual == anyo_cualquiera):
    print("Son los mismos anyos: ")
else:
    if(anyo_actual < anyo_cualquiera):
        print("Para llegar al año",anyo_cualquiera,"faltan",resultado,"año")
    else:
        if(anyo_actual > anyo_cualquiera):
             print("Desde el año",anyo_cualquiera,"han pasado",resultado,"año")
