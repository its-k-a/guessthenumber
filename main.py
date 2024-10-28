import random
random_num = random.randint(1, 10)
print("Random number between 1 and 10:", random_num)

while True:
    # TODO: Ask the user for a number using the int and the inputs functions.
    guess = int(input("Enter your guess: "))

    if guess > random_num:
        print("Too high!, Try again.")
    elif guess < random_num:
        print("Too low!, Try again.")
    else:
        print("Congratulations! You've guessed the number")
        break