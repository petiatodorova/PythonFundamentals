import re

text = input()
lst = list(filter(None, re.split(r"[, ;:.!()\"'/\[\]]+", text)))

lower_case = []
upper_case = []
mixed_case = []

for word in lst:
    if word == word.lower():
        lower_case.append(word)
    elif word == word.upper():
        upper_case.append(word)
    else:
        mixed_case.append(word)

print(f"Lower-case: ", end="")
print(", ".join(lower_case))
print(f"Mixed-case: ", end="")
print(", ".join(mixed_case))
print(f"Upper-case: ", end="")
print(", ".join(upper_case))