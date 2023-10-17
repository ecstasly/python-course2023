matrix = [
    [9, 8, 3],
    [7, 8, 6],
    [7, 7, 5]
]

# Обчислення середнього арифметичного для кожного рядка
average0 = round(sum(matrix[0]) / len(matrix[0]), 2)
average1 = round(sum(matrix[1]) / len(matrix[1]), 2)
average2 = round(sum(matrix[2]) / len(matrix[2]), 2)

# Створення списку середніх арифметичних
averages = [average0, average1, average2]

# Виведення середніх арифметичних
print(averages)

# Сортування матриці за зростанням середнього арифметичного
sorted_matrix = sorted(matrix, key=lambda row: sum(row) / len(row) , reverse = True)

# Виведення відсортованої матриці
for row in sorted_matrix:
    print(row)