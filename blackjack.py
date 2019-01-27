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

def play_again():
        global breaker
        again = input("do you want to play again [y] or [n]").lower()
        if again == "y":
            cleardeck()
            game()
        elif again == "n":
            print("bye")
            breaker = False
            return breaker

def make_deck():
    deck = []
    for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
        for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
            deck.append(Card(rank,suit))
    return deck

def deal(deck,person):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
        if person == "player":
            print(card)
    if person == "dealer":
        print(hand[1])
    return hand

def total_value(hand):
    total= 0
    if hand == player_hand:
        for card in hand:
            if card.rank == "ace":
                v = 0
                while v not in [1, 11]:
                    v = int(input("1 or 11?"))
                card.value = v
            total += card.value
        print(f"this is the value of the player's hand:{total}")
    elif hand == dealer_hand:
        for card in hand:
            if card.rank == "ace":
                v= 11
                card.value = v
            total += card.value
    return total

def deckshuffle(deck):
    while True:
        if len(deck) == 4:
             for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
                 for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
                     deck = []
                     deck.append(Card(rank,suit))
        else:
            break
        random.shuffle(deck)

def hit(hand,person):
    card = deck.pop()
    hand.append(card)
    if person == "player":
        for card in hand:
            print(card)
    elif person == "dealer":
        print (hand[1])
        print (hand[2])
    return hand

def results():
    print("This is was your hand:")
    for card in player_hand:
        print(card)
    print(f"and it adds up to: {total_value(player_hand)}")
    print("This was the dealer's hand:")
    for card in dealer_hand:
        print(card)
    cleardeck()

def blackjack(dealer_hand,player_hand):
    if total_value(dealer_hand) == 21:
        results()
        print("The dealer had blackjack. Good game you lose")
        play_again()
    elif total_value(player_hand) == 21:
        results()
        print("You had black jack congrats you won")
        play_again()

def score(dealer_hand, player_hand):
    if total_value(player_hand) == 21:
        results()
        print("Congratulations! You got Blackjack!")
    elif total_value(dealer_hand) == 21:
        results()
        print("Sorry, you lose. The dealer got Blackjack.")
    elif total_value(player_hand) > 21:
        results()
        print("Sorry. You busted. You lose.")
    elif total_value(dealer_hand) > 21:
        results()
        print("Dealer busts. You win!")
    elif total_value(dealer_hand) > total_value(player_hand):
        results()
        print("Sorry. Your score is lower than the dealers. You lose")
    elif total_value(player_hand) > total_value(dealer_hand):
        results()
        print ("Congratulations. Your score is higher than the dealer. You win")
    elif total_value(player_hand) == total_value(dealer_hand):
        results()
        print("It was a draw, Dealer wins")

def bust():
    global breaker
    if total_value(player_hand) > 21:
        results()
        print("Player Busts. You lose")
        play_again()
    elif total_value(dealer_hand) > 21:
        results()
        print("Dealer Busts. You win")
        play_again()
    else:
        pass

def cleardeck():
    garbage = []
    for card in player_hand:
        garbage.append(card)
        player_hand.pop(player_hand.index(card))
    for card in dealer_hand:
        garbage.append(card)
        dealer_hand.pop(dealer_hand.index(card))

def game():
    print(" ")
    print("Welcome to blackjack. Your goal is to get your hand to get as close to 21 or to be 21. But if you go over you go bust.")
    print(" ")
    player_input = input("Do you want to review the basics of blackjack, [y]es or [n]o: ").lower()
    print(" ")
    if player_input == "y":
        print("Now here are the basics,")
        print("     -All face cards equal 10 and an Ace can either equal 1 or 11 it is your choice")
        print("     -All number cards equal their number")
        print("     -When you are first delt the cards, your hand will show while the dealers hand has only one card showing")
        print("     -During the game you can hit, stay, or fold")
        print("         -Hitting adds a new deck to your hand, but it can be almost any card from an ace to king, so hit with caution")
        print("         -Staying means you dont want any more cards and youa and the dealer show cards and sees who wins")
        print("         -Folding means you gave up and the dealer automatically wins")
        print("     -To win the game you just have to have a higher value than the dealer or to get 21, but you go over you lose")
        print("     -If the game ends in a draw the dealer automatically wins")
    print(" ")
    global breaker
    choice = 0
    global deck
    global dealer_hand
    global player_hand
    breaker = True
    while breaker == True:
        deck = make_deck()
        deckshuffle(deck)
        print("This is your hand:")
        player_hand= deal(deck, "player")
        print("This is the dealer's hand:")
        dealer_hand= deal(deck, "dealer")
        blackjack(dealer_hand, player_hand)
        while breaker == True:
            choice = input("Do you want to [H]it, [S]tand, or [F]old: ").lower()
            if choice == "h":
                print("This is your new hand")
                player_hand = hit(player_hand,"player")
                total_value(player_hand)
                while total_value(dealer_hand) < 17:
                    hit(dealer_hand,"dealer")
                bust()
            elif choice == "s":
                while total_value(dealer_hand) < 17:
                    hit(dealer_hand,"dealer")
                bust()
                score(dealer_hand, player_hand)
                play_again()
            elif choice == "f":
                print("bye")
                breaker = False


game()
