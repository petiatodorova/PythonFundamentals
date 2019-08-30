first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# union operator | combines two sets to form a new one containing items in either
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first | second)

# intersection operator & gets items only in both
# {4, 5, 6}
print(first & second)

# difference operator - gets items in the first set but not in the second
# {1, 2, 3}
print(first - second)

# difference operator - gets items in the first set but not in the second
# {8, 9, 7}
print(second - first)

# symmetric difference operator ^ gets items in either set, but not both
# {1, 2, 3, 7, 8, 9}
print(first ^ second)