import random
import pygame

window = pygame.display.set_mode((700,700))
pygame.display.set_caption('Black Jack')

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
deck = make_deck()

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
        print (card)
    return hand
player_hand= deal(deck)
dealer_hand= deal(deck)

def total_value(hand):
    t= 0
    for i in range (len(hand)):
        t += hand[i].getvalue(hand[i].rank)
    if t <= 11 and (hand[0].getvalue()==1 or hand[1].getvalue()==1):
        t +=10 
    print(t)
    return t 
total_value(player_hand)


def deckshuffle(deck):
    while True:
        if len(deck) == 0:
             for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
                 for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
                     deck = []
                     deck.append(Card(rank,suit))

def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand

def cleardeck():
    garbage = []
    for card in player_hand:
        garbage.append(card)
        player_hand.pop(player_hand.index(card))
    for card in dealer_hand:
        garbage.append(card)
        dealer_hand.pop(dealer_hand.index(card))