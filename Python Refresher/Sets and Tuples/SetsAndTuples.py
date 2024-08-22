"""
Sets are similar to lists bu are unordered and connot contain duplicate elements.
Uses curly brackets
"""

my_sets = {1, 2, 3, 4, 5, 1, 2}
print(my_sets)
print(len(my_sets))

for x in my_sets:
    print(x)

my_sets.discard(3)
print(my_sets)
my_sets.add(6)
print(my_sets)
my_sets.update([7, 8])
print(my_sets)
my_sets.clear()
print(my_sets)
print()

"""
Tuples are similar to lists but are ordered and can contain duplicate elements.
Tuples are written in round brackets.
Tuples are faster than lists and it is immutable.
"""
my_tuple = (1, 2, 3, 4, 5, 1, 2)
print(my_tuple[0])
print(my_tuple)
print(len(my_tuple))

for x in my_tuple:
    print(x)