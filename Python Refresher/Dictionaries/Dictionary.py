"""
Dictionaries are used to store data values in key:value pairs.
"""
user_dictionary = {
    'username': 'admin',
    'name ': 'John',
    'age': 25
}
print(user_dictionary.get('username'))

user_dictionary['married'] = True
print(user_dictionary)

for x in user_dictionary:
    print(x)

for index, value in user_dictionary.items():
    print(index, value)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('age')
print(user_dictionary2)


user_dictionary.clear()
print(user_dictionary)