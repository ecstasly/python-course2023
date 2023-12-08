# Просимо користувача ввести шлях до файлу
file_path = input("Введіть повний шлях до текстового файлу: ")

# Зчитуємо вміст файлу з використанням кодування UTF-8
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Вводимо слова від користувача
while True:
    word1 = input("Введіть перше слово для заміни: ")
    word2 = input("Введіть друге слово на яке хочете змінити: ")

    # Перевіряємо, що користувач ввів обидва слова
    if not word1 or not word2:
        print("Помилка: Будь ласка, введіть обидва слова.")
    elif ' ' in word1 or ' ' in word2:
        print("Помилка: Будь ласка, введіть тільки одне слово для заміни.")
    else:
        # Замінюємо всі входження word1 на word2
        modified_content = content.replace(word1, word2)

        # Записуємо змінений текст назад у файл
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(modified_content)

        # Підраховуємо кількість змін
        occurrences = content.count(word1)
        print(f"Кількість змін: {occurrences}")
        
        # Выходим из цикла while
        break
