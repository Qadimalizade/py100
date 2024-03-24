numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_1 = numbers.copy()
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_1.pop(4)
average = sum(numbers_1) / len(numbers)
numbers[4] = average

print("Измененный список:", numbers)
