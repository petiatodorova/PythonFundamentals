import re

text = input()
regex_result = re.findall(r"[\w']+", text)
lower_case = []
upper_case = []
mixed_case = []

for word in regex_result:
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
