# Introducing List
from mimetypes import guess_type

shopping_list =['banana', 'apple', 'mango']
print(shopping_list)
print(shopping_list[2])
print(shopping_list[2].title())
print(shopping_list[-1])
# index -1 always returns the last element in a list
print(shopping_list[-2])
# index -2 returns the second last element in a list
message = "My favorite fruit is "
print(message + shopping_list[-1].title() + ".")

# EX: 3.1
friends = ['Savan', 'Uzair', 'Om', 'Greg', 'Dennis', 'David' , 'Stefan']
friends.sort()
print(friends[-1])
# EX: 3.2
message = ", whatcha been up to?"
print("Hey "+friends[3]+ message)
# EX: 3.3 SKIP

# EX: 3.4 - 3.7 Modified
# changing the list, adding to the list, removing from the list
pokemon_team = ['Charizard', 'Dragonite', 'Pikachu', 'Gengar', 'Lapras']
print(pokemon_team)
pokemon_team[2] = 'Jolteon'
print(pokemon_team)
pokemon_team.append('Snorlax')
print(pokemon_team)
pokemon_team.insert(3,'Mewtwo')
print(pokemon_team)
del pokemon_team[3]
print(pokemon_team)
popped_pokemon = pokemon_team.pop()
print(pokemon_team)
print(popped_pokemon)
print(pokemon_team.pop(3))
print(pokemon_team)
print(pokemon_team.remove('Jolteon'))
# reomves the first occurrence of the specified value
print(pokemon_team)
print('\n')

# EX: 3.8 - 3.10 Modified
# Organizing list
cars =['bmw', 'audi', 'ford', 'honda', 'toyota', 'subaru', 'farari']
print("non-destructive way")
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse = True))
print(cars)
print("destructive way")
cars.reverse()
print(cars)
cars.reverse()
print(cars)
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

print("length of a list")
print(len(cars))

