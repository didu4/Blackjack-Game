"""Блекджек против бота-дилера"""

import random

deck = [2,3,4,5,6,7,8,9,10,'A','J', 'Q', 'K'] * 4 # в колоде из Очка 52 карты; J - валет, Q - дама, K - король (все 10)
player_count = computer_count = 0
random.shuffle(deck)

"""card_names = {
    'J' : 'Jack',
    'K': 'King',
    'Q': 'Queen'
}"""


def cards_value(card):
    if card in ['J', 'Q', 'K']:  # if card in card_names:
        return 10
    elif card == 'A':
        return 11
    else:
        return card

def cards_count(cards):
    count = sum(cards_value(card) for card in cards)
    if count > 21 and 'A' in player_cards:
        count -= 10
    return count




player_cards = [deck.pop(), deck.pop()]
computer_cards = [deck.pop(), deck.pop()]

player_count = cards_count(player_cards)
computer_count = cards_count(computer_cards)


while True:

    print("Cards You have", player_cards)
    print("Your score:", player_count, "\n")
    choice = input("Would you like to take a card?\n").lower()
    if choice == 'yes':
        current_card = deck.pop()
        player_cards.append(current_card)
        player_count = cards_count(player_cards)

        if player_count > 21:
            print("\nCards You have", player_cards)
            print("Your score:", player_count)
            print("You've lost. Try again!")
            exit()

    elif choice == 'no':
        print("You refused to take the card. The game continues\n")
        break
    else:
        print('Wrong choice. Try again\n')
        continue

while computer_count < 17:
    current_card = deck.pop()
    computer_cards.append(current_card)
    computer_count = cards_count(computer_cards)

print("Cards Dealer has",computer_cards)
print("Score of the Dealer:",computer_count,"\n")

if computer_count > 21:
    print("\nCards You have",player_cards)
    print("Your score:", player_count)
    print("Cards Dealer has", computer_cards)
    print("Score of the Dealer:", computer_count, "\n")
    print("Congratulations! You've won!!!")

elif player_count > 21:
    print("\nCards You have",player_cards)
    print("Your score:", player_count)
    print("Cards Dealer has", computer_cards)
    print("Score of the Dealer:", computer_count, "\n")
    print("You've lost. Try again!")

elif computer_count > player_count:
    print("\nCards You have",player_cards)
    print("Your score:", player_count)
    print("Cards Dealer has", computer_cards)
    print("Score of the Dealer:", computer_count, "\n")
    print("You've lost. Try again!")

elif player_count > computer_count:
    print("\nCards You have",player_cards)
    print("Your score:", player_count)
    print("Cards Dealer has", computer_cards)
    print("Score of the Dealer:", computer_count, "\n")
    print("Congratulations! You've won!!!")

else:
    print("\nCards You have", player_cards)
    print("Your score:", player_count)
    print("Cards Dealer has", computer_cards)
    print("Score of the Dealer:", computer_count, "\n")
    print("It's a Draw.")









