import random
import os

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

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


def deal(deck,person):
    print("deal")
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
        if person == "player":
            print(card)
    if person == "dealer":
        print(hand[0])
    return hand

def total_value(hand):
    total= 0
    for card in hand:
        if card.rank == "ace":
            v = 0
            while v not in [1, 10]:
                v = int(input("1 or 11?"))
            card.value = v
        total += card.value
    # if total <= 11 and (hand[0].value ==1 or hand[1].value ==1):
    # if total >= 11:
    #     for card in hand:
    #         if card.value == 1:
    #             card.value = 10
    if hand == player_hand:
        print(total)
    return total



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
    for card in hand:
        print(card)
    return hand

def results():
    #global wallet
    print("results")
    print("This is was your hand:")
    for card in player_hand:
        print(card)
    print("This was the dealer's hand:")
    for card in dealer_hand:
        print(card)
    print(f"This now your wallet:[wallet]")
    cleardeck()

def blackjack(dealer_hand,player_hand):
    print("blackjack")
    blackjack = 1
    #global wallet 
    #global bet
    if total_value(dealer_hand) == 21:
       # wallet -= bet
        results()
        print("The dealer had blackjack. Good game you lose")
        blackjack = 0
    elif total_value(player_hand) == 21:
       # wallet += bet
        results()
        print("You had black jack congrats you won")
        blackjack = 0


def score(dealer_hand, player_hand):
    print("score")
   # global wallet
   # global bet
    if total_value(player_hand) == 21:
       # wallet += bet
        results()
        print("Congratulations! You got a Blackjack!")
    elif total_value(dealer_hand) == 21:
       # wallet -= bet
        results()
        print("Sorry, you lose. The dealer got a blackjack.")
    elif total_value(player_hand) > 21:
       # wallet -= bet
        results()
        print("Sorry. You busted. You lose.")
    elif total_value(dealer_hand) > 21:
       # wallet += bet
        results()
        print("Dealer busts. You win!")
        
    elif total_value(dealer_hand) > total_value(player_hand):
       # wallet -= bet
        results()
        print("Sorry. Your score is lowerd than the dealers. You lose")
    elif total_value(player_hand) > total_value(dealer_hand):
       # wallet += bet
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
    print("Welcome to blackjack. Your goal is to get your hand to get as close to 21 or to be 21. But if you go over you go bust.")
    choice = 0
    global deck
   # global wallet
   # global bet
    global dealer_hand
    global player_hand
   # wallet = 0
   # wallet = int(input("How much do you want to bring to the table:"))
   # bet = int(input("how much would you like to bet:"))
    breaker = True
    while breaker:
        deck = make_deck()
        deckshuffle(deck)
        player_hand= deal(deck, "player")
        dealer_hand= deal(deck, "dealer")
        blackjack(dealer_hand, player_hand)
        while blackjack == 1:
            blackjack(dealer_hand, player_hand)
            choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
            if choice == "h":
                player_hand = hit(player_hand)
            while total_value(dealer_hand) < 17:
                hit(dealer_hand)
            if choice == "s":
                while total_value(dealer_hand) < 17:
                    hit(dealer_hand)
                score(dealer_hand, player_hand)
                again = input("do you want to playy again [y] or [n]").lower()
                if again == "y":
                    cleardeck()
                    game()
                elif choice == "q" or again == "n":
                    print("bye")
                    breaker = False
       
game()