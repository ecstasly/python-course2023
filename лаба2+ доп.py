# Калькулятор слів і символів.
while True:
    # Запитайте користувача про текстовий рядок
    text = input("Введіть текстовий рядок: ")
# Перевірте, чи введено число або пробіли
    if not text.strip():
        print("Помилка: Введіть текстовий рядок.")
    elif text.isdigit():
        print("Помилка: В рядку не повинно бути цифр. Спробуйте ще раз.")
    else:
        break
# Розділіть введений рядок на слова за допомогою пробілів
words = text.split()
# Ініціалізуйте лічильники слів
word_count = len(words)
# Рядок для зберігання тексту з перевернутими словами
reversed_text = ""
 # Виведіть кількість слів
print("Кількість слів:", word_count)
# Виведіть слова та їх довжину (кількість символів)
for index , word in enumerate(words):
    if index % 2 == 1:  # Якщо індекс слова непарний (нумерація починається з 0)
        reversed_word = word[::-1]  # Перевернути слово
        reversed_text += reversed_word + " " # Додати перевернуте слово до рядку
        print(f"Слово {index + 1}: {reversed_word}, кількість символів: {len(reversed_word)}")
    else:
        reversed_text += word + " "  # Додати слово до рядку
        print(f"Слово {index + 1}: {word}, кількість символів: {len(word)}")
#Введіть текст з перевернутими словами
print("\nТекст з перевернутими словами:" , reversed_text)
#Кінець
print("Роботу завершено")