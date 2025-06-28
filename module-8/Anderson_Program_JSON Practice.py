import json

# Function to print students
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Load original JSON student list
with open('students.json', 'r') as file:
    students = json.load(file)

print("\n--- Original Student List ---")
print_students(students)

# Append your info
new_student = {
    "F_Name": "Zachary",
    "L_Name": "Anderson",
    "Student_ID": 99999,
    "Email": "zaanderson@my365.bellevue.edu"
}

students.append(new_student)

print("\n--- Updated Student List ---")
print_students(students)

# Save updated list back to file
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe students.json file has been updated.")
