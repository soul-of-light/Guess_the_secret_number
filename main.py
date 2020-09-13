secret = int("9")

guess = int(input("What is the secret number between 1 and 10? "))

if guess == secret:
    print("Congratulations, you've guessed it right!")
else:
    print("Sorry, but that's not correct.")
