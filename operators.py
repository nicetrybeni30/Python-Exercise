first_planet_input = int(input('Enter the distance from the sun for the first planet in km'))
second_planet_input = int(input('Enter the distance from the sun for the second planet in km'))

distance_km = first_planet_input - second_planet_input
print(abs(distance_km))