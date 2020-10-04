import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores:")

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3} The wrong guesses were {4}."\
        .format(score_dict.get("name"),
                str(score_dict.get("attempts")),
                score_dict.get("date"),
                score_dict.get("secret"),
                score_dict.get("wrong_guesses"))

    print(score_text)

print('Hi and welcome to "Guess the secret number".')
player_name = input("Please enter your player-name: ")

wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"name": player_name, "attempts": attempts, "wrong_guesses": wrong_guesses, "secret": secret,
                           "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)
