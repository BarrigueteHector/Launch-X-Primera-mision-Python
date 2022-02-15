new_planet = ""
planets = []

new_planet = input("Enter a planet: ")

while new_planet != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a planet or 'done' to exit: ")

print("Planets: %s" %(planets))