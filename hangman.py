import random

# Игра виселица
def hang_man(word):

    wrong = 0
    stages = ["",
              "______       ",
              "|     |      ",
              "|     |      ",
              "|     0      ",
              "|    /|\     ",
              "|    / \     ",
              "             "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    print("_ " * len(word))

    while wrong < len(stages) - 1:
        print("\n")
        char = input("Введите букву: ")
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"

        else:
            wrong += 1
            
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: {}".format(word))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("Вы проиграли! Было загадано слово: {}".format(word))

word_list = ["бобер", "овца", "робот", "собака", "попугай"]
word = random.randint(0,len(word_list)-1)
hang_man(word_list[word])
