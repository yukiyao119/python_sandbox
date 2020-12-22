# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Can't change value
# fruits[0]= 'Pears' # error

# Delete tuple
del fruits2

print(len(fruits), fruits2)



# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apple' in fruits_set)

fruits_set.add('Grape')
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete 
del fruits_set


