from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title('Blackjack')
root.geometry('500x500')

deck = [2,3,4,5,6,7,8,9,10,'A','J', 'Q', 'K'] * 4 # в колоде из Очка 52 карты; J - валет, Q - дама, K - король (все 10)
random.shuffle(deck)

player_cards = [deck.pop(), deck.pop()]
computer_cards = [deck.pop(), deck.pop()]

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

def update():
    player_label.config(text=f"Your cards: {player_cards}")
    player_score_label.config(text=f"Your score: {cards_count(player_cards)}")
    computer_label.config(text=f"Dealer's cards: [{computer_cards[0]}, ???]")
    computer_score_label.config(text="Score of the Dealer: ???")

def hit():
    player_cards.append(deck.pop())
    update()

    player_count = cards_count(player_cards)
    if player_count > 21:
        messagebox.showinfo("You've lost. Try again!")
        end_game()
    elif player_count == 21:
        messgebox.showinfo("Congratulations! You've won!!!")
        end_game()

def stand():
    while cards_count(computer_cards) < 17:
        computer_cards.append(deck.pop())

    player_count = cards_count(player_cards)
    computer_count = cards_count(computer_cards)

    computer_label.config(text=f"Dealer's cards: {computer_cards}")
    computer_score_label.config(text=f"Score of the Dealer: {computer_count}")

    result = ""
    if computer_count > 21 or player_count > computer_count:
        result = "Congratulations! You've won!!!"
    elif computer_count > player_count:
        result = "You've lost. Try again!"
    else:
        result = "It's a Draw."

    messagebox.showinfo("Game over.", f"Your score: {player_count}\nScore of the Dealer: {computer_count}\n{result}")
    end_game()

def end_game():
    hit_btn.config(state="disabled")
    stand_btn.config(state="disabled")



player_label = Label(root, text=f"Your cards: {player_cards}", font=("Arial", 16, "bold"))
player_label.pack(pady=5)
player_score_label = Label(root, text=f"Your score: {cards_count(player_cards)}", font=("Arial", 16, "bold"))
player_score_label.pack(pady=5)

computer_label = Label(root, text=f"Dealer's cards: [{computer_cards[0]}, ???]", font=("Arial", 16, "bold"))
computer_label.pack(pady=5)
computer_score_label = Label(root, text="Score of the Dealer: ", font=("Arial", 16, "bold"))
computer_score_label.pack(pady=5)

hit_btn = Button(root, text="Hit!", command = hit, font=("Arial", 16, "bold"))
hit_btn.pack(side="left",padx=20, pady=20)
stand_btn = Button(root, text="Stand!", command = stand, font=("Arial", 16, "bold"))
stand_btn.pack(side="right",padx=20, pady=20)

update()
root.mainloop()