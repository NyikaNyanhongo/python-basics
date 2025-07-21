# 1) Define the function "get_letter _grade(score)"- we are converting a
#    number grade into a letter grade 

def get_letter_grade(score):
    if score > 90:
        return 'A'
    elif score > 80: 
        return 'B'
    elif score > 70:
        return 'C'
    elif score > 60:
        return 'D'
    else: 
        return 'F'
    

# 2) Define the function "print_summary(student_list)"- we need to display a list 
#     of students showing the name, the scoe and the letter grade 

def print_summary(student_list):
    print("Student Information List: ")
    for student in student_list:
        print(f"{student['name']}: {student['score']} {student['grade']}")

# 3) Define the function "save_to_file(student_list)" - we are using this to save 
#     this info to a file called grades.txt IN WRITE MODE 'w'

def save_to_file(student_list):
    with open("geades.txt","w") as file:
        for student in student_list:
            file.write(f"{student['name']}: {student['score']} {student['grade']}")

            