def add_student():
    with open("students.txt", "a") as file:
        last_name = input("Прізвище студента: ")
        first_name = input("Ім'я студента: ")
        average_grade = input("Середній бал успішності: ")
        file.write(f"{last_name} {first_name} {average_grade}\n")
    print("Студента додано.")

def remove_student():
    last_name = input("Прізвище студента, якого потрібно видалити: ")
    with open("students.txt", "r") as file:
        lines = file.readlines()
    with open("students.txt", "w") as file:
        for line in lines:
            if last_name not in line:
                file.write(line)
    print("Студента видалено.")

def change_student_info():
    last_name = input("Прізвище студента, інформацію якого потрібно змінити: ")
    new_info = input("Введіть нову інформацію про студента: ")
    with open("students.txt", "r") as file:
        lines = file.readlines()
    with open("students.txt", "w") as file:
        for line in lines:
            if last_name in line:
                file.write(new_info + "\n")
            else:
                file.write(line)
    print("Інформацію про студента змінено.")

def show_all_students():
    with open("students.txt", "r") as file:
        students = file.read()
    print("Список студентів:")
    print(students)

def search_student():
    search_param = input("Введіть параметр пошуку (прізвище, ім'я тощо): ")
    with open("students.txt", "r") as file:
        students = file.readlines()
    print("Результати пошуку:")
    for student in students:
        if search_param in student:
            print(student.strip())

def sort_students():
    sort_order = input("Введіть порядок сортування (за алфавітом, за середнім балом тощо): ")
    with open("students.txt", "r") as file:
        students = file.readlines()
    sorted_students = sorted(students, key=lambda student: student.split()[2] if sort_order == "за середнім балом" else student)
    print("Відсортовані студенти:")
    for student in sorted_students:
        print(student.strip())

def excellent_students():
    with open("students.txt", "r") as file:
        students = file.readlines()
    excellent_students = [student.strip() for student in students if float(student.split()[2]) >= 10]
    print("Відмінники:")
    for student in excellent_students:
        print(student)

while True:
    print("\nМеню:")
    print("1. Додати студента")
    print("2. Видалити студента")
    print("3. Змінити інформацію про студента")
    print("4. Показати на екрані ВСІХ студентів")
    print("5. Вивести на екран інформацію про студента, виконавши пошук за вказаним параметром")
    print("6. Вивести студентів в певному порядку")
    print("7. Вивести 'відмінників'")
    print("0. Вийти з програми")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        change_student_info()
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        search_student()
    elif choice == "6":
        sort_students()
    elif choice == "7":
        excellent_students()
    elif choice == "0":
        break
    else:
        print("Неправильний вибір. Спробуйте знову.")
