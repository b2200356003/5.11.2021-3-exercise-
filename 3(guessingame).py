import random
number=random.randrange(1,25)
guess=int(input("Guess a number:"))

while guess != number:
    if guess < number:
        guess=int(input("Choose a bigger one:"))
    elif guess> number:
        guess=int(input("Choose a smaller one:"))

print("You quess it correctly !!!")




