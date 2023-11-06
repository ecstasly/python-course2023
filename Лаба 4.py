class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_avg_grade(self):
        return sum(self.grades) / len(self.grades)

class StudingGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)

    def display_info(self):
        print("\nСписок студентів:")
        for student in self.students:
            avg_grade = student.get_avg_grade()
            print(f"Ім'я студента: {student.name}, Середня оцінка: {avg_grade}")

# Створюємо обьекти класа  Student и добавляємо їх в групу 
student1 = Student("Назар", [5, 4, 5, 3, 4])
student2 = Student("Артем", [4, 4, 3, 5, 5])
student3 = Student("Дмитро", [3, 4, 4, 4, 5])
student4 = Student("Гліб", [5, 5, 5, 5, 5])

group = StudingGroup()
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.add_student(student4)

group.display_info()

# Добавляємо нового студента
student5 = Student("Ірина", [5, 5, 4, 4, 5])
group.add_student(student5)

# Виводимо список після добавлення
group.display_info()

# Видаляємо студента по імені
group.remove_student("Артем")

# Виводимо список після видалення
group.display_info()