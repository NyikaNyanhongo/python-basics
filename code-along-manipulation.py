string1 = 'This is a valid string'
string2 = "This is a valid string"
#string3 = 'This is NOT a valid string-see why?''

palindrome = "Go hand a salami, l'm a lasagna hog"

# Using a quote inside a string

string3 = "'Always look at the bright side of life ' - Monty Python"

# Use escape characters to include quotes in strings

string4 ="\"Always look on the Bright side of life\" - Monty Python"
print(string4)

print(len(string4))

name = "      Micheal  " 
print(len(name))
print(name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print(name_no_spaces)
print("Hello " + name_no_spaces)

#split()

filepath = "/var/micheal/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

#usecase

fullname = "Micheal, Vanderpool"
names = fullname.split(",")
row ="Micheal Vanderpool, 49, 6'4\""
#print(names):['Michael' , 'Vanderpool']
firstname = names[0]
lastname =names[1]

#join

windowsPath = "||".join(folders)
print(windowsPath)

#find()

reservation_name = "Froman, Abe"
char_to_find = ","
#where is the coma?

char_location = reservation_name.find(char_to_find)
print(char_location)

#index()

reservation_name = "Froman, Abe"
char_to_find = ","
#where is the coma?

char_location = reservation_name.index(char_to_find)
print(char_location)

#transformations

print(reservation_name.upper())
print(reservation_name.lower())
print(reservation_name.title()) #captalizes first letter
print(reservation_name.swap())#swaps lowercase letter to uppercase and vice-versa
print(reservation_name.capitalize())

#f-strings

name = "Michael"
age = 49

print(f"My name is {name} and l am {age} years old.") 
print("My name is "+ name + " and l am " + str(age) + "years old.")
a=3
b=9
#rint(f'We can count to {b} by {a}: 
      

#replacing 

name = "Micael Vanderpoole"
name = name.replace ("Micael" , "Michael") 
name = name.replace("Vanderpoole", "Vanderpool")
print(name)  