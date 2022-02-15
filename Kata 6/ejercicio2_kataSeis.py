planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

input_planet = input("Add a planet to the list: ")
planets.append(input_planet)
print("Possition of %s: %d" %(input_planet, planets.index(input_planet)))

planets_before_earth = planets[:planets.index(input_planet)]
print("Planets before %s: %s" %(input_planet, planets_before_earth))

planets_after_earth = planets[planets.index(input_planet)+1:]
print("Planets after %s: %s" %(input_planet, planets_after_earth))