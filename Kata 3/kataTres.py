#EJERCICIO 1
velocidadAsteroide = 49
if velocidadAsteroide > 25:
    print("!!!ADVERTENCIA!!!\nEl asteroide es muy rapido")
else:
    print("El asteroide tiene una velocidad menor o igual a 25 km/h, no es peligroso")

#EJERCICIO 2
velocidadAtmosfera = 19
if velocidadAtmosfera >= 20:
    print("El asteoride producira un rayo que se podra ver en la tierra")
else:
    print("La velocidad del asteroide en la atmosfera es menor a 20 km/h")

#EJERCICIO 3
velocidadAsteroide2 = 55
dimensionAsteroide = 50

if velocidadAsteroide2 > 25 and dimensionAsteroide > 25 and velocidadAsteroide2 < 1000:
    print("!!!PELIGRO!!!\nEl asteroide causara daño en la tierra")
elif velocidadAsteroide2 > 25:
    print("!!!ADVERTENCIA!!!\nEl asteroide es muy rapido")
elif dimensionAsteroide > 25 and velocidadAsteroide2 < 1000:
    print("!!!PELIGRO!!!\nEl asteroide es muy grande y causara daño en la tierra")
elif dimensionAsteroide > 1000:
    print("!!!PELIGRO!!!\nEl asteroide es más mayor de 1000 metros")
else:
    print("El asteroide no presenta ningun peligro para la tierra")