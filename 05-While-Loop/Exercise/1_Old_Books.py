book_wanted = input()
book = input()

count_of_books = 0

while book != 'No More Books':
    if book == book_wanted:
        print(f'You checked {count_of_books} books and found it.')
        break
    book = input()
    count_of_books += 1
else:
    print(f'The book you search is not here!')
    print(f'You checked {count_of_books} books.')