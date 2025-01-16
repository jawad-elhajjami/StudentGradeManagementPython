# Title : Student Grade Management
# Author : EL HAJJAMI JAWAD
# Version : 1.0

# list of dictionaries storing students information
students = []

# function to add student to list
def add_student(name, grades):
    # check if parameter "grades" is a list o numbers
    if not isinstance(grades, list) or not all(isinstance(grade, (int, float)) for grade in grades):
        print("Error : grades must be a list of numbers")
        return
    students.append({"name":name, "grades":grades})
    print("Student Added successfully !")

# Calculates and returns the average grade for a specific student.
def calculate_average(name):
    # get grades
    grades = []
    for student in students:
        if student["name"] == name:
            grades = student["grades"]
            average = sum(grades) / len(grades)
            return float(round(average, 2))
    return f"Error: Student '{name}' not found."

# Finds and returns the name of the student with the highest average grade.
def find_top_student():
    if not students:
        return "No students Found"
    return max(students, key=lambda x: calculate_average(x["name"]))["name"]

#Displays all students and their grades.
def display_students():
    count = 1
    for student in students:
        avgGrade = calculate_average(student['name'])
        print(f"Student N{count} || \t Name : {student['name']} || Grade: {avgGrade} \t")
        count += 1
        

# Add students
add_student("Alice", [85, 90, 78])
add_student("Bob", [92, 88, 91])
add_student("Charlie", [100, 100, 100])

# Display all students
display_students()

# Calculate average grade for a student
print("Alice's average grade:", calculate_average("Alice"))

# Find the top student
print("Top student:", find_top_student())