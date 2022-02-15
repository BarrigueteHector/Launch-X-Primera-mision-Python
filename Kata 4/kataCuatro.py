#EJERCICIO 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

lista = text.split(".")
#print(lista)

claves = ["average", "temperature", "distance"]

for parte in lista: #Recorre la lista
    for c in claves: #Recorre la lista de claves
        if c in parte: #Si la clave esta en la parte
            #print(parte) ->DESBLOQUEAR PARA VER LA SALIDA ORIGINAL
            break

for parte in lista:
    for c in claves:
        if c in parte:
            print(parte.replace('C', 'Celsius'))
            break

print("\n")

#EJERCICIO 2
#PRUEBA 1
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

#PRUEBA 2
name = "Ganimedes"
gravity = 0.00143 # in kms
planet = "Marte"

titulo = "gravity facts about " + name
conversionG = gravity * 1000
plantilla = "%s\n---------------------------------------------\nPlanet Name: %s\nGravity on %s: %s m/s2" % (titulo.title(), planet, name, conversionG)

#PRIMERA FORMA
#print("%s\n---------------------------------------------\nPlanet Name: %s\nGravity on %s: %s m/s2" % (titulo.title(), planet, name, conversionG))

#SEGUNDA FORMA
print(plantilla)