# Матриця
matrix = [
    [2, 2, 3],
    [8, 5, 6],
    [7, 8, 9]
]

# Функція для обчислення середнього арифметичного значення рядка
def average_of_row(row):
    return sum(row) / len(row)

# Вивід середнього арифметичного значення кожного рядка
for i, row in enumerate(matrix):
    avg = round(average_of_row(row),2)
    print(f"Середнє арифметичне рядка {i + 1}: {avg}")
# Вивід відсорт рядка за зростанням середнього арифметичного значення  
sorted_matrix = sorted(matrix, key=average_of_row, reverse=True)
for row in sorted_matrix:
    print(row)