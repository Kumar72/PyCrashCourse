# Working with Lists

# EX: 4.1
pizzas = ['Veggie Lovers', 'Buffalo Chicken', 'Meat Lovers', 'Mediterranean']
for pizza in pizzas:
    print(pizza.title())
print('I can eat pizza for days!\n')
# the colon indicated the start of a for loop
# indent only when you are suppose to, as it is part of certain syntax ex. for loop
# main cause of logical errors in python

# EX: 4.2
animals = ['lion', 'leopard', 'tiger', 'cheetah']
for cat in animals:
    print('A '+cat.title()+' would make a nice pet.')
print('Which cat would you pick as your pet?\n')

# EX: 4.3
for value in range(1,20):
    print(value)

# EX: 4.4 - 4.5
# using range() & list() function together
numbers = list(range(1,1000))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# EX: 4.6
odd_numbers = list(range(1,20,2))
for odd in odd_numbers:
    print(odd)
# we start the list at 2 and end at 11 and we are adding 2 every time

# EX: 4.7
multiplication_list = [value*3 for value in range(1,11)]
print(multiplication_list)
for table in multiplication_list:
    print(table)

# EX: 4.8
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# EX: 4.9 list comprehension
cube_comprehension = [value**3 for value in range(1,11)]
print(cube_comprehension)

# EX: 4.10 slicing a list
games = ['horizon zero dawn','fall out 4', 'far cry 4', 'skyrim', 'oblivion', 'witcher 3: wild hunt', 'GTA 5']
print("\nMy current list of open world games on my PS4: ")
for game in games[:3]:
    print(game.title())
print('\nMy list of PS3 open world games: ')
for game in games[3:5]:
    print(game.title())
print('\nGames I look forward to playing today: ')
for game in games[5:]:
    print(game.title())

# EX: 4.11 copying a list
friend_games = games[:]
games.append('Battlefield 1')
friend_games.append('Destiny: Collection')
print('\nMy list of games: ')
print(games)
print("\nMy friend's list of games: ")
print(friend_games)

# EX: 4.12 SKIP

# immutable list of objects is called a tuple and they use () instead of []
# EX: 4.13
buffet = ('Sushi', 'Burger', 'Pizza', 'Noodles' , 'Curry')
for meal in buffet:
    print(meal)
# you can reuse the variable by assigning it something new but the original list cannot be overwritten
buffet = ('American', 'Chinese', 'Japanese', 'Indian', 'Mexican')
for meal in buffet:
    print(meal)

