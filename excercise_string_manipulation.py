#Qsn 1 
#split values into individual values 
to_be_changed = " John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison ".split('|')
changed_values = to_be_changed
print(changed_values)

#Qsn2
#split the lysics by line using split()
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
""".split("\n")
lyrics_split = lyrics
print(lyrics_split)

#Qns 3
#Split the lyrics by line using something other than split().
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
""".index("\n") #correct way is to use lyrics.splitlines()
changed_values = lyrics
print(changed_values)


#Qsn4
#How long is the long village name string?
long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

#Qns5 
#We want all folders in this path without additional spaces. How would you get that?
my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM '
my_folders = my_path.strip().split("/")
print(my_folders)

#Qsn6 
#Given this list of names, change the third name in the list to be "Wolfgang Mozart".
composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers = composers.replace('Mozart,Wolfgang', 'Wolfgang Mozart')
print(composers)

# Separate the composers
composers_split = composers.split(";")
print(composers_split) 

# Get the third composer
third_composer = composers_split[2]
print(third_composer)


# Find the comma in the name
comma_position = third_composer.find(",")
print(comma_position)


# Use the slicing notation to get the last name
#last_name = third_composer[]

# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name  + " " +  last_name
print(f"{first_name} {last_name}")
print(full_name)


# Print the composer's name
#print(third_composer_name)
