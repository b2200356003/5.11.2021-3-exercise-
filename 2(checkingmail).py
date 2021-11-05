#Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for the sake of simplicity).
#Use that function to check if a user input is a valid e-mail or not.

email:None
def checkmail ():
    usermail= input("Please write your e mail adress:")
    for letter in usermail:
        if letter=="@":
            email=True
        elif letter ==".":
            email=True
        else: email=False
    print(email)


checkmail()
