book_name = input()
capacity = int(input())

count = 0

while True:
    count += 1
    if count > capacity:
        print(f'The book you search is not here!')
        print(f'You checked {count - 1} books.')
        break
    current_book = input()

    if current_book == book_name:
        print(f'You checked {count - 1} books and found it.')
        break


