'''our_number = 42

is_guessed = False
# the while loop runs until condition turns true 

while is_guessed == False:

#get input from the user

 guess = int(input("Enter your guess: "))

#conditional statements to check the guess

if guess == our_number:
    print('Hooray!')
    is_guessed = True
elif guess > our_number:
    print('Too High!')
else: 
    print('Too Low!')

# Stop light

color = "Red"

if color == "Red":
    print("Stop!")
else:
    print("Go")

# game over

health = 100 

while health >=0
   
if health <= 0:
    print('Game Over!')'''



'''counter = 1 
while counter < 20:
    if counter % 3 == 0 and counter % 5 == 0: 
        print(f'{counter}: Fizzbuzz')
        break
    elif counter % 3 == 0:
        print(f'{counter}: Fizz')
    elif counter % 5 == 0: 
        print(f'{counter}: Buzz')

        counter = counter + 1 '''
        

        # for loop example
loop_range = range(1 , 11)
for i in loop_range:
    print(f'Iteration {i}')

print(max(loop_range))

# for loop with a list 
fruits = ['apples','banana','cherry',3,4.5]

for i in fruits:
    print(f'Fruit: {i}')

favorite_movies = ['inception', 'The Matix', 'Interstellar']

for movie in favorite_movies:
    print(f'Movie: {movie}')

numbers = [1, 11, 111, 12, 34, 35]

for value in numbers:
    print()