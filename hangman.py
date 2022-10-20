# 8 stage

import random

mylist = ["python", "java", "javascript", "php"]
mylist1 = []
mylist2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = random.choice(mylist)
wordsep = list(word)
tire = ["-" for i in wordsep]
tryagain = 8


print("HANGMAN\n")

while True:
    game = input("\nType 'play' to play the game, 'exit' to quit:")

    if game == "play":
        while True:
            print("".join(tire))
            b = input("Input a letter: >")

            if b in mylist1:
                print("You've already guessed this letter.\n")
            mylist1.append(b)

            if len(b) != 1:
                print("You should input a single letter.\n")
                continue

            if b not in mylist2:
                print("Please enter a lowercase English letter.\n")
                continue

            if b in wordsep:
                for i, c in enumerate(wordsep):
                    if c == b:
                        tire[i] = b

                if "-" not in tire:
                    print(word)
                    print("You guessed the word!\nYou survived!")
                    break

            else:
                tryagain -= 1
                print("\nThat letter doesn't appear in the word")

            if tryagain == 0:
                print("\nYou lost!")
                break

    if game == "exit":
        break





















