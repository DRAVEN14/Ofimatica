print("Menu de Gasolina")
print("Super:Normal (1,5€), Turbo (1,55€)")
print("Sin plomo:Normal (1,6€), Con aditivos(sabor naranja) (1,65€)")
print("Diesel:Normal (1,7€), Fast&Furius (1,75€)")
super_normal=1
super_turbo=2
sin_plomo_normal=3
sin_plomo_con_aditivos=4
diesel_normal=5
diesel_fast_furius=6
gasolina=int(input("Elige que tipo de gasolina quieres: "))
litros=int(input("Cuantos litros quieres: "))
if(gasolina==1):
    res_1=(litros*1.5)
    print("Total a pagar",res_1,"€")
else:
    if(gasolina==2):
        res_2=(litros*1.55)
        print("Total a pagar",res_2,"€")
    else:
        if(gasolina==3):
            res_3=(litros*1.6)
            print("Total a pagar",res_3,"€")
        else:
            if(gasolina==4):
                res_4=(litros*1.65)
                print("Total a pagar",res_4,"€")
            else:
                if(gasolina==5):
                    res_5=(litros*1.7)
                    print("Total a pagar",res_5,"€")
                else:
                    if(gasolina==6):
                        res_6=(litros*1.75)
                        print("Total a pagar",res_6,"€")
                        
    
