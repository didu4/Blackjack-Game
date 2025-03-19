"""Соло-версия Блекджека"""
import random

deck = [2,3,4,5,6,7,8,9,10,'A','J', 'Q', 'K'] * 4 # в колоде из Очка 52 карты; J - валет, Q - дама, K - король (все 10)
count = 0
random.shuffle(deck)

while True:
    choice = input("Would you like to take a card?\n").lower()
    if choice == 'yes':
        current_card = deck.pop()
        card_names = {
            'J' : 'Jack',
            'K': 'King',
            'Q': 'Queen'
        }
        if type(current_card) is int:

            print("You've got a %d card!"%current_card)
            count += current_card

        elif current_card in card_names:
            print(f"You've got a {card_names[current_card]}!")
            count += 10

        elif current_card == 'A':
            print("You've got an Ace!")
            if count >= 11:
                count += 1
            else:
                count += 11

        print("You have %d points now" % count)
        if count > 21:

            print("You've lost. Try again!")
            break
        elif count == 21:

            print("Congratulations! You've won!!!")
            break


    elif choice == 'no':
        print("You have %d points and the game is over. Try again!"%count)
        break
