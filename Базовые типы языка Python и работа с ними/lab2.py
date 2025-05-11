pages = 100
lines = 50
chars = 25
bytes_per_char = 4

book_size = pages * lines * chars * bytes_per_char
floppy_size = 1.44 * 1024 * 1024
num_books = int(floppy_size // book_size)

print("Количество книг, помещающихся на дискету:", num_books)