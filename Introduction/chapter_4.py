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

# range() function
for value in range(1,20):
    print(value)


