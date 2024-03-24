# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
line_in_pages = 50
symbol_in_line = 25
symbol_in_book = pages * line_in_pages * symbol_in_line
memory = symbol_in_book * 4

disk_mb = 1.44
disk_kb = disk_mb * 1024
disk_b = disk_kb * 1024

book_in_disk = disk_b // memory
print("Количество книг, помещающихся на дискету:", int(book_in_disk))

# Стоит ли создавать столько одноразовых переменных?
