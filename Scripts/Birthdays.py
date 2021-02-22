birthdays = {'Bob': 'July 7th', 'Jill':'April 17th'}
while True:
	print('Enter a name')
	name = input()
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
		break
	else:
		print('I dont have the birthday info for that person')
		print('What day is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('updated birthday database')
	
