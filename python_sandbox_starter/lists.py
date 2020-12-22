# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5]

# Use constructor
numbers2 = list((1,2,3,4,5))
fruits = ['Apples', 'Orange', 'Grapes', 'Pears']


# Get a value
print(fruits[1])

print(len(fruits))

fruits.append('Mangos')

fruits.remove('Grapes')

fruits.insert(2, 'Strawberries')

fruits[0] = 'Blueberries'

fruits.pop(2)

fruits.reverse()

fruits.sort()

# Reverse sort
fruits.sort(reverse=True)



print(fruits)
