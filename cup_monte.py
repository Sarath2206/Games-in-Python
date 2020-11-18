#Import random
from random import shuffle

#Game Rules
print("@@@ Game Rules @@@")
print("s = 5 points")
print("n = 10 points")
print("_ = -5 points --- You Lose a life ")

#Calculate scores
def set_score(choice, cups, score, lives):
    if cups[choice-1] == 's':
        score += 5
    elif cups[choice-1] == 'n':
        score += 10
    else:
        lives -= 1
    return (score, lives)


#Play The Game
def play_game():
    score, lives = 0, 3
    cups = ['_']*5
    cups[:2] = ['n', 's']
    while lives>0:
        choice = int(input("Enter your choice: "))
        if choice<1 or choice>5:
            print("Wrong Choice")
        else:
            shuffle(cups)
            print(cups)
            score, lives = set_score(choice, cups, score, lives)
            print(f'Your score = {score}\nRemaining lives = {lives}')
    return score

print(f'Congratulations... Your total score is {play_game()}')

