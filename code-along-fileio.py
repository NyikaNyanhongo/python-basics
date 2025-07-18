file_path = 'data.csv'

print(file_path)

file = open(file_path, 'r') #open in read mode 
file = open(file_path, 'w') #open in write mode 
file = open(file_path, 'a') #open in append mode
file = open(file_path, 'r+') #open in read/write mode

#write function will create a new file or overwrite an existing one 
file = open("example2.txt", "w")
file.write("Hello , World!\n")
file.write("This is line two!\n")
file.close()

#open a file using the 'With' keyword

with open("example-with.txt", "w") as file:
    file.write("We wrote this file using the 'with' keyword")
    file.write("This is line two!")
    file.write("This is line three!")



#read funtion to read the contents of a file 
with open ("example-with.txt", 'r') as file: 
    contents = file.read()
    print(contents)

#use for loop  to read from a file 

with open("example-with.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append to a file using 'with'

with open("example-with.txt", "a") as file:
    file.write("This is an append line\n")