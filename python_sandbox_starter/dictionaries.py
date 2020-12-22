# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person ={
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# person2 = dict(first_name='Sara', last_name='Williams')


# print(person, type(person))
# print(person['first_name'])
# print(person.get('last_name')) 

person['phone'] = '555-555-5555'

# print(person.keys())
# print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Delete item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

print(len(person2))

# print(person)

# List of dict
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25},
]

print(people[0]['name'])



