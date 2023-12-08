while True:
    # Вводимо шлях до файлу від користувача
    file_path = input("Введіть повний шлях до текстового файлу (або введіть 'exit' для виходу): ")

    # Перевіряємо, чи користувач хоче вийти
    if file_path.lower() == 'exit':
        break

    try:
        # Зчитуємо вміст файлу з використанням кодування UTF-8
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        break  # Якщо файл успішно зчитано, виходимо з циклу
    except FileNotFoundError:
        print("Помилка: Файл не знайдено. Перевірте введений шлях та спробуйте ще раз.")

while True:
    # Вводимо слова від користувача
    word1 = input("Введіть перше слово для заміни (або введіть 'exit' для виходу): ")

    # Перевіряємо, чи користувач хоче вийти
    if word1.lower() == 'exit':
        break

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
