# importing libraries
import sys
import select
from faker import Faker
import enchant
f = Faker()

#user input within fixed amount of time
def get_user_input(timeout_seconds):
    global playerWord

    # Use select to implement a timeout for input
    rlist, _, _ = select.select([sys.stdin], [], [], timeout_seconds)

    if rlist:
        playerWord = sys.stdin.readline().strip()
    else:
        print("# 5 sec's up!")
        print("# Game over!")
        print(f'# points: {points}')
        return 0


# checking valid word
def is_word(word):
    englishDictionary = enchant.Dict("en_US")
    return englishDictionary.check(word)
words = list()


# predefining wordlist
for i in range(1000):
    words.append(f.word())

points = 0


# initial condition
playerUsedWords = list()
computerWord = words[0]
words.remove(computerWord)
print(computerWord)

words.sort()
words = list(set(words))


# main game loop
while(1):
    if get_user_input(5): break
    playerWord = playerWord.lower()

    # checking game ending conditions
    if not is_word(playerWord):
        print("# not a valid word!")
        print("# Game over!")
        print(f'# points: {points}')
        break
    elif playerWord in playerUsedWords:
        print("# Already used word!")
        print("# Game over!")
        print(f'# points: {points}')
        break
    elif playerWord[0]!=computerWord[-1]:
        print("#character doesn't match!")
        print("# Game over!")
        print(f'# points: {points}')
        break

    # game continuation
    else:
        points+=1
        playerUsedWords.append(playerWord)
        for i in words:
            if playerWord[-1]==i[0]:
                computerWord = i
                words.remove(i)
                print(computerWord)
                break
