import random
deckOfCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
playerHand = []
computerHand = []



def testWin():
    if sum(playerHand) == sum(computerHand):
        print("Draw")
    elif sum(playerHand) == 21:
        print("Blackjack! You win")
    elif sum(computerHand) == 21:
        print("Computer has blackjack you lose")

    if sum(playerHand) > 21:
        if sum(computerHand) < 21:
            print("You lost")
        elif sum(computerHand) > 21:
            print("Draw")
    elif sum(computerHand) > 21:
        if sum(playerHand) < 21:
            print("You win")
        elif sum(playerHand) > 21:
            print("Draw")
    elif sum(playerHand) < 21:
        if sum(computerHand) > 21:
            print("You win!")
        elif sum(computerHand) < sum(playerHand):
            print("You win")
        else:
            print("You lost")


def drawPlayerCard():
        playerHand.append(random.randint(0,9))
        print("Your Cards are:", playerHand)
        print("total:", sum(playerHand), "\n")
        if len(playerHand) < 2:
            drawPlayerCard()
        else:
            drawComputerCard()


def drawComputerCard():
    if sum(computerHand) <= 17:
        computerHand.append(deckOfCards[random.randint(0, 9)])
        print("the computer has:", computerHand)
        print("total:", sum(computerHand), "\n")
        if len(computerHand) < 2:
            drawComputerCard()
        else:
            hit_stand()
    else:
        print("the computer stands with a total of:", sum(computerHand))
        hit_stand()


def hit_stand():
        option = input("do you want to hit or stand? [h/s]")
        if option.lower() == "h":
            drawPlayerCard()
        elif option.lower() == "s":
            testWin()
        else:
            print("please say if you want to hit or stand!")
            hit_stand()


def start():
    start_gaming = input("Do you want to play Blackjack? [y/n]")
    if start_gaming == "y":
        drawPlayerCard()
    elif start_gaming == "n":
        pass
    else:
        print("please state if you want to start the game")
        start()


start()
