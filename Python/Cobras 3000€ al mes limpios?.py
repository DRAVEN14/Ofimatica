loteria = input("Has ganado la loteria: ")
milloneti = input("Te has casado(a)con un milloneti: ")
edad = int(input("Cuanta edad tiene: "))
corazon = input("Tiene problemas de corazon: ")
casado = input("Esta casado(a): ")
M01 = int(input("Cuanta nota tienes en M01: "))
M02 = int(input("Cuanta nota tienes en M02: "))
M03 = int(input("Cuanta nota tienes en M03: "))
M05 = int(input("Cuanta nota tienes en M05: "))
media_ponderada = (M01*0.3 + M02*0.4 + M03*0.25 + M05*0.05)

if(loteria =="si")or(milloneti =="si" and edad >=80 and corazon =="si" and casado =="si")or(M01 >=9 and M02 >=10 and M03 >=8)and(M05 >=6 and M05 <=8)or(media_ponderada >8):
    print("Cobras 3000€ al mes limpios")
else:
    print("Eres un parguela no cobras 3000€ al mes limpios")
