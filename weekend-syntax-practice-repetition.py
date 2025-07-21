'''#Create variables for your name, age, pi value, and student status.
#Print each variable.

name ="Nyika Nyanhongo"
age = 25
pi_value = 3.14159
is_student = True

print (name)
print(age)
print(pi_value)
print(is_student)

     
#Ask for a favorite number 
favorite_number = input("Enter you favorite number: ")
#Convert and print it as int and float.
favorite_number_int = int(favorite_number)
favorite_number_float = float(favorite_number)
print(favorite_number_float)
print(favorite_number_int)
#Ask for an item price, calculate 5% tax, and print total price.
price = float(input("Please enter price of item: "))
tax = (price * 0.05)
total_price = price + tax 
print (f'The total price is: ${total_price:.2f}')'''

'''#ask for name and formati it
your_name = input("Please enter you name : ")
print(your_name.title())
#convert sentenses to lowercase and uppercase
print("pYthOn iS fUn!".lower()) #makes the sentence all lower case
print(your_name.upper()) #makes all upercase'''

#Lists
#create my_fruits and add 3 fruits
my_fruits = []
my_fruits.append("Banana")
my_fruits.append("Apple")
my_fruits.append("Grape") 
print(my_fruits)
#access first item
print(my_fruits[0])
#Create a student_grades list of mini lists
student_grades = [ ["John","English", 85] , ["Harry", "Geography", 90] , ["Jacob", "Math",99]]
for students in student_grades:
    print(f"Name: {students[0]} , Subject: {students[1]} , Score: {students[2]}")