# Ім'я вхідного файлу
#FILENAME = "task.txt"

# Ім'я вихідного файлу (відформатований текст)
output_file_path = r"C:\Users\Користувач\OneDrive\Рабочий стол\formatted_text.txt"

# Виведення початкового тексту з файлу
print("Початковий текстовий файл:")
with open(r"C:\Users\Користувач\OneDrive\Рабочий стол\task.txt", encoding="utf-8") as file:
    text = file.read()
    print(text)

# Безкінечний цикл для введення обмеження довжини тексту
while True:
    # Введення обмеження довжини тексту користувачем
    user_input = input("\nВведіть обмеження довжини тексту (або 'exit' для виходу): ")

    # Перевірка на вихід з програми
    if user_input.lower() == "exit":
        break
    else:
        try:
            # Спроба перетворити введене значення на ціле число
            text_limit = int(user_input)
        except ValueError:
            # Виведення повідомлення про помилку, якщо введено не число
            print("Будь ласка, введіть ціле число або 'exit'.")

    # Розділення тексту на слова
    words = text.split()
    formatted_lines = []
    current_line = ""

    # Проходження по словам і форматування тексту
    for word in words:
        if len(current_line) + len(word) <= text_limit:
            current_line += word + " "
        else:
            formatted_lines.append(current_line.rstrip())
            current_line = word + " "

    # Додавання останнього рядка тексту до відформатованого списку
    formatted_lines.append(current_line.rstrip())

    # Запис відформатованого тексту у файл
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(formatted_lines))

    # Виведення відформатованого тексту в консоль
    print("Відформатований текст:")
    with open(output_file_path, encoding="utf-8") as file2:
        formatted_text = file2.read()
        print(formatted_text)