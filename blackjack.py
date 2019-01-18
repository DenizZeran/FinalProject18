import random
import os

def clear():
    os.system('cls')

class Card:
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.getvalue(rank)

    def getvalue(self,rank):
        values = {'ace':1,'two':2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}
        return values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"



def make_deck():
    print("make_deck")
    deck = []
    for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
        for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
            deck.append(Card(rank,suit))
    return deck


def deal(deck):
    print("deal")
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
        print (card)
    return hand


def total_value(hand):
    t= 0
    for i in range (len(hand)):
        t += hand[i].getvalue(hand[i].rank)
    if t <= 11 and (hand[0].getvalue(hand[0].rank)==1 or hand[1].getvalue(hand[1].rank)==1):
        t +=10
    print(t)
    return t



def deckshuffle(deck):
    print("shuffle")
    while True:
        if len(deck) == 4:
             for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
                 for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
                     deck = []
                     deck.append(Card(rank,suit))
        else:
            break
        random.shuffle(deck)

def hit(hand):
    print("hand")
    card = deck.pop()
    hand.append(card)
    return hand

def results():
    print("results")
    print("This is was your hand:")
    for card in player_hand:
        print(card)
    print("This was the dealer's hand:")
    for card in dealer_hand:
        print(card)
    cleardeck()

def blackjack(dealer_hand,player_hand):
    print("blackjack")
    if total_value(dealer_hand) == 21:
        results()
        print("The dealer had blackjack. Good game you lose")
    elif total_value(player_hand) == 21:
        results()
        print("You had black jack congrats you won")

def score(dealer_hand, player_hand):
    print("score")
    if total_value(player_hand) == 21:
        results()
        print("Congratulations! You got a Blackjack!")
    elif total_value(dealer_hand) == 21:
        results()
        print("Sorry, you lose. The dealer got a blackjack.")
    elif total_value(player_hand) > 21:
        results()
        print("Sorry. You busted. You lose.")
    elif total_value(dealer_hand) > 21:
        results()
        print("Dealer busts. You win!")
    elif total_value(dealer_hand) > total_value(player_hand):
        results()
        print("Sorry. Your score is lowerd than the dealers. You lose")
    elif total_value(player_hand) > total_value(dealer_hand):
        results()
        print ("Congratulations. Your score is higher than the dealer. You win")

def cleardeck():
    print("clear deck")
    garbage = []
    for card in player_hand:
        garbage.append(card)
        player_hand.pop(player_hand.index(card))
    for card in dealer_hand:
        garbage.append(card)
        dealer_hand.pop(dealer_hand.index(card))

def game():
    print("game")
    choice = 0
    global deck
    global dealer_hand
    global player_hand
    breaker = True
    while breaker:
        deck = make_deck()
        deckshuffle(deck)
        player_hand= deal(deck)
        dealer_hand= deal(deck)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        score(dealer_hand,player_hand)
        again = input("do you want to paly again [y] or [n]").lower()
        if again == "y":
            deck = make_deck()
            player_hand = []
            dealer_hand = []
        elif choice == "q" or again == "n":
            print("bye")
            breaker = False
game()