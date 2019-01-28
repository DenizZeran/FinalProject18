import random
#This class to establish what the cards are thier suit, rank, and the value that they hold
# It also contains a function to get the value of any card for use later in the game
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
#This function allows the player to chose on whether they would like to countinue playing or not
# If the player says yes, then the functions clears the deack and hands and resets the round
#If the player says no it gives the value that breaks all the loops
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
# This function fills the deck using the card class created before. It makes it so there is 52 cards, with 13 of each suit.
def make_deck():
    deck = []
    for suit in ['spades', 'diamonds', 'hearts', 'clubs']:
        for rank in ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']:
            deck.append(Card(rank,suit))
    return deck
# this function is for dealing cards to the two hands. It shuffles the deck and takes one card out and plops it into the hand.
#It does the process twice, and when writing this line you have to specifiy what person it is for.
#this is so the function knows what cards to show in terminal, if it is player it will show the full hand, but if it is dealer it will only show the second card.
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
#THis function is for calculating the total value of the hands using self.value from the card class
def total_value(hand):
    global total
    total= 0
    # The function is split in two for the two diferent hands, for player hand it allows the player to chose the value for the ace,
    #while for the dealer it is automatically 11
    if hand == player_hand:
        for card in hand:
            #In blackjack Ace could equal 11 or 1 this if statement allows the player to chose what value they want
            if card.rank == "ace":
                v = 0
                while v not in [1, 11]:
                    v = int(input("1 or 11?"))
                card.value = v
                #the card new value is then set equal to card and added to the total adn prints it out
            total += card.value
        print(f"this is the value of the player's hand:{total}")
    elif hand == dealer_hand:
        for card in hand:
            if card.rank == "ace":
                v= 11
                card.value = v
            total += card.value
    return total
# the function watches the amount of cards in the deck and if it ever gets to 4 left it will empty and then refill the deck and then it will shuffle the deck
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
#the function takes a card out of the deck list and puts it into the hand
#this function is also split in two due the different printing of the hands
# printing every card in player hands
# printing the already printed card and the newly added card
def hit(hand,person):
    card = deck.pop()
    hand.append(card)
    if person == "player":
        print("Player's hand:")
        for card in hand:
            print(card)
    elif person == "dealer":
        print("dealer's hand")
        print (hand[1])
        print (hand[2])
    return hand
# this function is for the end showing the results of the game
# It shows what was in the players and dealers hand and shows what the players final total was for the player. It then procceds to clear the deck.
def results():
    global total
    print("This is was your hand:")
    for card in player_hand:
        print(card)
    print(f"and it adds up to: {total_value(player_hand)}")
    print("This was the dealer's hand:")
    for card in dealer_hand:
        print(card)
    cleardeck()
#Checks the two hands right after the cards are delt if they got black jack it's when the total value equals 21 with and ace and face or ten card
#Checks both player and dealer hand and if it triggers one it shows the results using the result function and then uses the play again function to restart.
def blackjack(dealer_hand,player_hand):
    if total_value(dealer_hand) == 21:
        results()
        print("The dealer had blackjack. Good game you lose")
        play_again()
    elif total_value(player_hand) == 21:
        results()
        print("You had black jack congrats you won")
        play_again()
#this function checks the two hands for every winning, losing, and draw scenerio
# for each if/elif statement it prints the results and a message letting the player know what happened
# this only comes to play at the end of the round
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
#Like the black jack function this function checks each hand, however this functions checks to seeif they busted.
# it comes in after hiting and if triggered will show the results() and a message and then asks you if you want to playagain()
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
# this function clears the hands by taking the cards in the hands and appending them to the garbage list
def cleardeck():
    garbage = []
    for card in player_hand:
        garbage.append(card)
        player_hand.pop(player_hand.index(card))
    for card in dealer_hand:
        garbage.append(card)
        dealer_hand.pop(dealer_hand.index(card))
# this the final game function it combines all the other functions into one
def game():
    print(" ") # a little intro line
    print("Welcome to blackjack. Your goal is to get your hand to get as close to 21 or to be 21. But if you go over you go bust.")
    print(" ")# Just incase the the player doesn't know how to play the game offers a review of the rules of black jack
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
    breaker = True#sets up all the global variabples
    while breaker == True:#first loop to keep the game going
        deck = make_deck()# Here the game sets the deck and the two hands
        deckshuffle(deck)
        print("This is your hand:")
        player_hand= deal(deck, "player")
        print("This is the dealer's hand:")
        dealer_hand= deal(deck, "dealer")
        blackjack(dealer_hand, player_hand) # checks for black jack
        while breaker == True: #second loop allows the player to hit more than once
            choice = input("Do you want to [H]it, [S]tand, or [F]old: ").lower()# asks the player what they want to do hit stay or fold
            if choice == "h":#player gets a new card and if the dealer total is less than 17 it aoutmatically hits the dealer hand
                print("This is your new hand")
                player_hand = hit(player_hand,"player")
                total_value(player_hand)
                while total_value(dealer_hand) < 17:
                    hit(dealer_hand,"dealer")
                bust()# checks if plaher or dealer busts
            elif choice == "s":# player stays and it checks if the dealer needs to get hit
                while total_value(dealer_hand) < 17:
                    hit(dealer_hand,"dealer")
                bust()
                score(dealer_hand, player_hand)#checks to see what happened and lets the player know
                play_again()# asks to re start the game
            elif choice == "f":# folding ends all the loops and restarts not the round but the game
                print("bye")
                breaker = False# both loops are set to break when breaker = false


game() #the game
