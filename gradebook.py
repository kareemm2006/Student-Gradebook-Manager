import numpy as np
# القواميس الرئيسية
student = {}
assignment = []
# حساب معدل طالب
def calculate_student_average(grades):
    return np.mean(grades) if grades else 0.0
# حساب معدل الصف لكل مهمة
def calculate_class_average(student:dict):
    if not student:
        return np.array([])
    if not assignment:
        return np.array([])
    grades = np.array(list(student.values()))
    return np.mean(grades, axis=0)
# حساب أعلى وأقل درجة لكل مهمة
def calculate_max_min_average(student:dict):
    if not student:
        return np.array([]),np.array([])
    grades = np.array(list(student.values()))
    grades_max = np.max(grades, axis=0)
    grades_min = np.min(grades, axis=0)
    return grades_max, grades_min
# عرض النتائج
def display_results(student:dict , assignment:dict):
    if not student:
        print("\n No students available.")
        return
    if not assignment:
        print("\n No assignments available.")
        return
    print("\n Student Gradebook\n")
    print("Student".ljust(15), "Grades".ljust(30), "Average")
    print("-" * 60)
    for name,grades in student.items():
        avg = calculate_student_average(grades)
        print(str(name).ljust(15), str(grades).ljust(30), f"{avg:.2f}")
    print("\n Class Averages for Assignments:")
    class_avg = calculate_class_average(student)
    for task, avg in zip(assignment, class_avg):
        print(f"{str(task).ljust(15)} {avg:.2f}")
    max_vals, min_vals = calculate_max_min_average(student)
    print("\n Max/Min Grades for Assignments:")
    for task, max_val, min_val in zip(assignment, max_vals, min_vals):
        print(f"{str(task).ljust(15)} Max: {max_val:.2f}  Min: {min_val:.2f}")
# إدارة الطلاب
def manage_student():
    print('\nManage Student:')
    print('1. Add Student')
    print('2. Remove Student')
    choice = input('Enter your choice: ')
    if not choice.isdigit():
        print('Invalid input, please enter a number.')
        return
    choice = int(choice)
    if choice == 1:
        name = input('Enter student name: ').strip()
        if name in student:
            print('Student already exists.')
            return
        if len(assignment) == 0:
            print('Add assignments first.')
            return
        try:
            grades = []
            for task in assignment:
                grade = float(input(f'Enter grade for {task}: '))
                grades.append(grade)
            student[name]=grades
            print(f"Student '{name}' added successfully.")
        except ValueError:
            print('Invalid input. Please enter numeric grades.')
    elif choice == 2:
        name = input('Enter the name: ')
        if name in student:
            del student[name]
            print(f"Student '{name}' was removed.")
        else:
            print('Name not found.')
# إدارة المهام
def manage_assignment():
    global student , assignment
    print('\nManage Assignment:')
    print('1. Add Assignment')
    print('2. Remove Assignment')
    choice = input('Enter your choice: ')
    if not choice.isdigit():
        print('Invalid input, please enter a number.')
        return
    choice = int(choice)
    if choice == 1:
        task = input('Enter assignment name: ').strip()
        if task in assignment:
            print('Assignment already exists.')
            return
        assignment.append(task)
        for name in student:
            try:
                grade = float(input(f"Enter grade for '{task}' for student '{name}': "))
                if 0<= grade<=100:
                 student[name][task] =grade
                else:
                    print('Grade must be between  0 and 100')
            except ValueError:
                print('Invalid grade. Setting default value 0.0')
                student[name][task]= 0.0
        print(f"Assignment '{task}' added.")
    elif choice == 2:
        task = input('Enter assignment name: ').strip()
        if task not in assignment:
            print('Assignment not found.')
            return
        index = assignment.index(task)
        assignment.remove(task)
        for name in student:
            try:
                del student[name][index]
            except IndexError:
                pass
        print(f"Assignment '{task}' removed.")
# عرض حالة الصف
def show_class_state():
    if not student:
        print('No students in the class.')
        return
    if not assignment:
        print('No assignments have been added.')
        return
    print('\n Class State:')
    print(f'Total students: {len(student)}')
    print(f'Total assignments: {len(assignment)}')

    avg_grades = calculate_class_average(student)
    print("\nAverage grade per assignment:")
    for task, avg in zip(assignment, avg_grades):
        print(f"{task}: {round(avg, 2)}")

# القائمة الرئيسية
def main_program_loop():
    while True:
        print('\n Welcome to the Student Gradebook Manager')
        print('1. View Grades')
        print('2. Add/Remove Student')
        print('3. Add/Remove Assignment')
        print('4. Show Class State')
        print('5. Exit')
        choice = input('Choose an option (1-5): ')
        if not choice.isdigit():
            print('Please enter a number between 1 and 5.')
            continue
        choice = int(choice)
        if choice == 1:
            display_results(student,assignment)
        elif choice == 2:
            manage_student()
        elif choice == 3:
            manage_assignment()
        elif choice == 4:
            show_class_state()
        elif choice == 5:
            print("Goodbye! ")
            break
        else:
            print('Invalid choice, please select from 1 to 5.')
            
 # تشغيل البرنامج
if __name__=="__main__":
    main_program_loop()
