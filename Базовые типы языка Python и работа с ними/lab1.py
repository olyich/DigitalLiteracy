numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# Находим индекс пропущенного элемента
missing_index = numbers.index(None)

# Вычисляем сумму всех элементов, кроме None
sum_without_none = sum(num for num in numbers if num is not None)

# Вычисляем среднее арифметическое
average = sum_without_none / len(numbers)

# Заменяем None на среднее арифметическое
numbers[missing_index] = average
print("Измененный список:", numbers)
