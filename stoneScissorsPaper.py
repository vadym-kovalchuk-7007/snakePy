from sys import exit
from random import randint

sci = ["н", "Ножиці"]
sto = ["к", "Камінь"]
pap = ["б", "Бумага"]
ex = ["в", "Вихід"]
elements = [sci, sto, pap]
choices = [i[0] for i in elements]
wins = 0
losses = 0
ties = 0
winPairs = [[sto[0], sci[0]], [pap[0], sto[0]], [sci[0], pap[0]]]
userName = "Користувач"
compName = "Комп'ютер"


def printCurElement(player, choice):
    currIndx = choices.index(choice)
    print("%s обрав %s" % (player, elements[currIndx][1]))


def printWinner(player):
    print("%s виграв" % (player))


while True:
    print("\n %s перемог, %s поразок, %s ніч`я" % (wins, losses, ties))
    while True:
        print("Оберіть (н)ожиці, (б)умага, (к)амінь або (в)вихід")
        userChoice = input()
        if userChoice == ex[0]:
            print(userName, ex[1])
            exit()
        if userChoice in choices:
            printCurElement(userName, userChoice)
            break
        else:
            continue
    compChoice = choices[randint(0, len(choices) - 1)]
    printCurElement(compName, compChoice)
    if userChoice == compChoice:
        ties += 1
        print("ніч'я")
        continue
    else:
        hasWinner = False
        for winPair in winPairs:
            if userChoice == winPair[0] and compChoice == winPair[1]:
                wins += 1
                printWinner(userName)
                hasWinner = True
                break
    if not hasWinner:
        printWinner(compName)
        losses += 1
