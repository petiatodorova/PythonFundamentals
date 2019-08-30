'''    •  If the message contains only digits you should replace each two digit number with the ASCII character that represents it and print
 "Reviewing item – {item}", where {item} is the decoded message.
    •  If the message contains only letters you should print:
"Reviewing location – {location}", where location is the encoded message but reversed.'''

n = int(input())
m = float(input())
count_of_reviews = 0

for num in range(n):
    encoded_message = input()

    if encoded_message.isdigit():
        encoded_message = int(encoded_message)
        rev_string = []
        while encoded_message > 0:
            last_two_nums = encoded_message % 100
            rev_string.append(last_two_nums)
            encoded_message = encoded_message // 100

        name = list(map(lambda a: str(chr(a)), list(reversed(rev_string))))
        the_name = "".join(name)
        print(f"Reviewing item - {the_name}")
        count_of_reviews += 1

    elif encoded_message.isalpha():
        print(f"Reviewing location - {encoded_message[::-1]}")
        count_of_reviews += 1

    else:
        continue

salary = count_of_reviews * m
print(f"{count_of_reviews} reviews have been made this month. Salary: {salary:.2f}")
