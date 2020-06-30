
import random
import string
str1 = string.ascii_lowercase  


def check(word, blank_list):  # for checking the winner of the game
    word = set(word)
    blank_list = set(blank_list)
    return word == blank_list


print('''H A N G M A N''')
word_list = ['python', 'java', 'kotlin', 'javascript']  # list of words
comp = random.choice(word_list)  # random words
blank_list = ["-"] * len(comp)   # blank list
typed_letters = []
chances = 8
game = 'play'
while game == 'play':   # main loop
    game = input('Type "play" to play the game, "exit" to quit: ')
    while chances != 0:
        print("\n"+"".join(blank_list))
        name = input("Input a letter: ")
        

        if name in typed_letters:
            print("You already typed this letter")


        elif name in blank_list and name != "-":
            print("You already typed this letter")
            if name == "-":
                pass
            else:
                typed_letters.append(name)


        elif name in comp:   # putting the letters in the word
            new = []
            for x in range(len(comp)):
                if name == comp[x]:
                    new.append(x)
            for x in new:
                blank_list[x] = name
            if name == "-":
                pass
            else:
                typed_letters.append(name)


        elif len(name) != 1 :
            print("You should input a single letter")
            

        elif name not in str1:
            print("It is not an ASCII lowercase letter")
            
        elif name not in comp:
            print("No such letter in the word")
            if name == "-":
                pass
            else:
                typed_letters.append(name)

            chances -= 1

        b = check(comp, blank_list)

        if b == True:
            print(f'You guessed the word {"".join(blank_list)}!')
            print('You survived!\n')
            break
        elif b == False and chances == 0:
            print("You are hanged!\n")
