from itertools import product, permutations

letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print(list(permutations(letters)))