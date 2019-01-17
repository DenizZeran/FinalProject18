import random

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
    deck = []
    for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
        for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
            deck.append(Card(rank,suit))
    return deck


def deal(deck):
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
    while True:
        if len(deck) == 4:
             for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
                 for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
                     deck = []
                     deck.append(Card(rank,suit))
        random.shuffle(deck)

def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand

def results():
    print("This is was your hand:")
    for card in player_hand:
        print(card)
    print("This was the dealer's hand:")
    for card in dealer_hand:
        print(dealer_hand)
    cleardeck()
    
def blackjack(dealer_hand,player_hand)
    if total_value(dealer_hand) == 21:
        results()
        print("The dealer had blackjack. Good game you lose")
    elif total_value(player_hand) == 21:
        results()
        print("You had black jack congrats you won")



def cleardeck():
    garbage = []
    for card in player_hand:
        garbage.append(card)
        player_hand.pop(player_hand.index(card))
    for card in dealer_hand:
        garbage.append(card)
        dealer_hand.pop(dealer_hand.index(card))

def game():
    while True:
        deckshuffle()
        player_hand= deal(deck)
        dealer_hand= deal(deck)
        deck = make_deck()
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            deck = make_deck()
            player_hand = []
            dealer_hand = []
        elif again == "n"
            print("bye")
            break
