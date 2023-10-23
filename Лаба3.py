# Початкове поле
print("Ось початкове поле: ")
# Початковий стан поля
field = [
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
    ['.'] * 12,
]

# Координати X на полі
x_coords = [(1, 1), (3, 1), (2, 2), (1, 3), (3, 3)]

# Початкове розташування символу "X"
def x_field(field, coords):
    for x, y in coords:
        field[y][x] = 'X'

x_field(field, x_coords)

# Виведення поля
for row in field:
    print(" ".join(row))

# Цикл переміщення X
while True:
    move = input("\nВведіть команду (напрямок та відстань, наприклад 'вгору 2' та якщо хочете выйти, напишіть 'exit'), щоб перемістити X: ")
    if move == 'exit':
        break
    parts = move.split()
    
    if len(parts) == 2:
        direction = parts[0]
        distance = int(parts[1])

        # Переміщення X по всім координатам
        for i in range(len(x_coords)):
            x, y = x_coords[i]
            new_x, new_y = x, y  # Создаем новые переменные для хранения новых координат

            if direction == 'вгору':
                new_y -= distance
            elif direction == 'вниз':
                new_y += distance
            elif direction == 'вліво':
                new_x -= distance
            elif direction == 'вправо':
                new_x += distance

            # Проверяем, чтобы новые координаты находились в пределах поля
            if 0 <= new_x < 12 and 0 <= new_y < 9:
                x_coords[i] = (new_x, new_y)  # Сохраняем новые координаты только если они в пределах поля
            else:
                print("Помилка: X виходить за межі поля.")
                break

        # Очистити поле і встановити нове розташування X
        field = [['.'] * 12 for j in range(9)]
        x_field(field, x_coords)

        # Виведення поля з новим розташуванням X
        for row in field:
            print(" ".join(row))
    else:
        print("Неправильний формат команди. Спробуйте ще раз.")

    