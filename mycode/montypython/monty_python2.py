#!/usr/bin/env python3
round = 0
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer.capitalize() == "Brian":
        print("correct")
        break
    elif round == 3:
        print("sorry the answer was Brian.")
        break
    else:
        print("Sorry try again")
