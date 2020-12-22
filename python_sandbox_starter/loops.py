# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

for person in people:
  if person == 'Sara':
    break
  print(f'current person: {person}')


for person in people:
  if person == 'Sara':
    continue                # skip Sara and call Susan
  print(f'current person: {person}')


for i in range(len(people)):
  print(people[i])

# for i in range (0, 11):
#   print(f'Number: {i}')         # print from 0 to 10




# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1