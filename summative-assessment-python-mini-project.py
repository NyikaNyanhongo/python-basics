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

#Main Program  
def main():
#PRINT welcome message
print("Welcome to the Grade Tracker program!")
     
#CREATE empty list called students
students = []
# WHILE user wants to continue:#ASK for student name & 
# FORMAT name (capitalize properly)
while True:
    name = input("Enter name of student: ").strip()
    name = name.title()


#ASK for score
#CONVERT score to number (float or int)
#VALIDATE input (optional error check)
while True:
            try:
                score_input = input("Enter score (0–100): ")
                score = float(score_input)
                if 0 <= score <= 100:
                    break
                else:
                    print("Try again, Input a score between 0 and 100!!")
            except ValueError:
                print("Input not  Valid. Please enter a number....!")


#CALL get_letter_grade(score) to get grade

grade = get_letter_grade(score)

#ADD (name, score, grade) to students list: here we add collected input to empty list we created 
students.append({"name": name, "score": score, "grade": grade})

#ASK user if they want to add another student
cont = input("\nDo you want to add another student? (Y/N): ")
cont = cont.upper() 
if cont != "Y":
   break 
# AFTER loop ends:
#CALL print_summary(students)
#CALL save_to_file(students)
#PRINT "Data saved" message
print("\nStudent data saved to grades.txt")