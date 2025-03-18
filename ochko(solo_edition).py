"""Упрощенная соло-версия игры в Блекджек aka Очко"""
import random

deck = [6,7,8,9,10,'A','J', 'Q', 'K'] * 4 # в колоде из Очка 36 карт; J - валет (2), Q - дама (3), K - король (4)
count = 0
random.shuffle(deck)

while True:
    choice = input("Would you like to take a card?\n").lower()
    if choice == 'yes':
        current_card = deck.pop()
        if type(current_card) is int:

            print("You've got a %d card!"%current_card)
            count += current_card

        elif current_card == 'J':
            print("You've got a Jack!")
            count += 2

        elif current_card == 'Q':
            print("You've got a Queen!")
            count += 3

        elif current_card == 'K':
            print("You've got a King!")
            count += 4

        elif current_card == 'A':
            ace = input("You've got an Ace. Now choose its value:\n")
            while (ace != '1') and (ace != '11'):
                ace = input("Wrong value: ace must have 1 or 11 value\n")
            count += int(ace)


        if count > 21:
            print("You have %d points now" % count)
            print("You've lost. Try again!")
            break
        elif count == 21:
            print("You have %d points now" % count)
            print("Congratulations! You've won!!!")
            break
        else:
            print("You have %d points now"%count)

    elif choice == 'no':
        print("You have %d points and the game is over. Try again!"%count)
        break
