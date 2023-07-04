"""
Belloni Lucio
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos"""

tarifa = 15000
estacion_del_año = input("Ingresar la estacion en la que queres ir Invierno/Verano/Otoño/Primavera: ")
estacion_del_año = estacion_del_año.lower()
while estacion_del_año != "invierno" and estacion_del_año != "verano" and estacion_del_año != "otoño" and estacion_del_año != "primavera":
    estacion_del_año = input("Error, Ingresar la estacion corespondiente Invierno/Verano/Otoño/Primavera: ")
localidad = input("Ingrese una localidad Bariloche/Cataratas/Mar del Plata/Córdoba: ")
localidad = localidad.lower()
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad !=  "cordoba":
    localidad = input("Eror, Ingrese una localidad Bariloche/Cataratas/Mar del Plata/Córdoba: ")

match estacion_del_año:
    case "invierno":
        if localidad == "bariloche":
            bariloche_aumento =  tarifa * 1.2
            print("bariloche con aumento es: ", bariloche_aumento )
        elif localidad == "cataratas" and "cordoba":
            descuesto_cordoba_y_cataratas = tarifa * 0.90
            print("descuesto cordoba y cataratas: ", descuesto_cordoba_y_cataratas )
        elif localidad == "mar del plata":
            descuesto_mar_del_plata = tarifa * 0.80
            print("mar del plata con descuesto es: ", descuesto_mar_del_plata)
    case "verano":
        if localidad == "bariloche":  
            bariloche_descuento = tarifa * 0.80
            print("en verano bariloche con descuesto es: ", bariloche_descuento)
        elif localidad == "cataratas" and localidad == "cordoba":
            aumento_cordoba_cataratas = tarifa * 1.10
            print("En verano cordoba y cataratas con su aumento es de: ", aumento_cordoba_cataratas)
        elif localidad == "mar del plata":
            aumento_mar_del_plata =  tarifa * 1.20
            print("Mar del plata en verano con su aumento es de: ", aumento_mar_del_plata)
    case other:
        if localidad == "bariloche":
            bariloche_aumento_other = tarifa * 1.10
            print("otoño y primavera en bariloche con su descuesto es: ", bariloche_aumento_other)
        elif localidad == "cataratas":
            cataratas_aumento = tarifa * 0.90
            print("otoño y primavera en cataratas con su aumento es de: ", cataratas_aumento )
        elif localidad == "mar del plata":
            aumento_mar_del_plata_other = tarifa * 1.10
            print("otoño y primavera en mar del plata con su aumento es de: ",aumento_mar_del_plata_other )
        else:
            cordoba_sin_descuento = tarifa
            print("otoño y primavera en cordoba sin descuesto es de: ", cordoba_sin_descuento)





    
    



