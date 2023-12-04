import hashlib

desktop_path = r'C:\Users\Користувач\OneDrive\Рабочий стол'

def hash_password(password):
    # Хэшируем пароль с использованием SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

while True:
    enter = input("Вітаю, щоб продовжити, введіть 1 або 2 (для виходу введіть 'exit'): ")

    if enter.isdigit() and 0 < int(enter) < 3:
        if enter == '1':
            while True:
                nickname = input("Введіть нікнейм: ")

                if not nickname:
                    print("Помилка: поле нікнейму не може бути порожнім.")
                elif len(nickname) < 3:
                    print("Помилка: нікнейм повинен містити принаймні 3 символи.")
                elif len(nickname) > 32:
                    print("Помилка: довжина нікнейму не може перевищувати 32 символи.")
                elif any(c in nickname for c in [' ', ':', '"', "'"]):
                    print("Помилка: нікнейм не може містити пробіли, двокрапки або лапки.")
                elif nickname.isdigit():
                    print("Помилка: нікнейм не може складатися тільки з цифр.")
                else:
                    break  # Нікнейм валідний, вийти з циклу
                м 
            while True:
                password = input("Введіть пароль: ")
                confirm_password = input("Підтвердіть пароль: ")

                if not password or not confirm_password:
                    print("Помилка: поля паролю не можуть бути порожніми.")
                elif len(password) < 8:
                    print("Помилка: пароль повинен містити принаймні 8 символів.")
                elif password != confirm_password:
                    print("Помилка: пароль та підтвердження паролю не співпадають.")
                else:
                    # Хэшируем пароль и сохраняем в файл
                    hashed_password = hash_password(password)
                    user_file_path = f"{desktop_path}\\{nickname}.txt"
                    with open(user_file_path, "w") as user_file:
                        print(f"Нікнейм: {nickname}", file=user_file)
                        print(f"Хеш пароля: {hashed_password}", file=user_file)
                    
                    print("Реєстрація успішна. Нікнейм:", nickname)
                    break  # Реєстрація успішна, вийти из цикла
        elif enter == '2':
            nickname = input("Введіть нікнейм: ")
            password = input("Введіть пароль: ")

            user_file_path = f"{desktop_path}\\{nickname}.txt"

            try:
                with open(user_file_path, "r") as user_file:
                    saved_nickname = user_file.readline().strip()
                    saved_hashed_password = user_file.readline().strip().split(": ")[1]

                # Хэшируем введенный пароль и сравниваем с сохраненным хешем
                hashed_password = hash_password(password)
                if saved_nickname == f"Нікнейм: {nickname}" and saved_hashed_password == hashed_password:
                    print("Вхід успішний. Даний користувач знаходиться в базі.")
                else:
                    print("Помилка: неправильний пароль.")
            except FileNotFoundError:
                print("Помилка: користувача із заданим нікнеймом не існує.")
        else:
            print("Будь ласка, введіть 1 або 2")
    elif enter.lower() == 'exit':
        break
    else:
        print("Будь ласка, введіть 1 або 2 або 'exit'")