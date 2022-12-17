import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)  # from Deck.deal() --> single card(suit, rank)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, balance=1000):
        self.balance = balance
        self.bet = 0

    def take_bet(self):
        while True:
            try:
                bet = int(input("How much would you like to bet today?"))
                if bet > self.balance:
                    print("Sorry, your bet cannot exceed: {}".format(self.balance))
                else:
                    self.bet = bet
                    break
            except ValueError:
                print("Sorry, you entered an invalid input. a bet must be a positive integer!")
                break

    def win_bet(self):
        self.balance += self.bet

    def lose_bet(self):
        self.balance -= self.bet


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter H or S ')  # HIT # hh # stand

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0] == 's':
            print("Player Stands, Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter 'h' or 's' only!")
            continue
        break


def show_some(player, dealer):
    # dealer.cards[0] is hidden. [1] is shown
    # show only ONE of the dealer's cards
    print("\nDealer's Hand: ")
    print("first card hidden!")
    print(dealer.cards[1])
    # show all (2 cards) of the player's hand
    print("\nPlayer's hand: ", *player.cards, sep="\n")
    print("Player's hand = ", player.value)


def show_all(player, dealer):
    # show all the dealer's card
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)
        """ print("\nDealer's hand: ", *dealer.cards, sep = "\n")"""  # this line does the same by iterating through
        # dealer's hand and print them as requested with SEPARATOR of \n!
    # calculate and display value (J+K == 20)
    print("Value of Dealer's hand is : {}".format(dealer.value))
    # show all the player's hand
    print("\nPlayer's hand: ", *player.cards, sep="\n")
    print("Value of Player's hand is : {}".format(player.value))


def player_busts(chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! PUSH")


"""---GAME LOGIC---"""
player_chips = Chips()
# an opening statement:
print("--------------------WELCOME TO BLACKJACK--------------------")
print("*#" * 30)
print("*  TRY TO REACH AS CLOSE TO 21 AS POSSIBLE WITHOUT PASSING  *")
print("*   YOU CAN CALL HIT FOR MORE CARDS OR STAND. PLAY WISELY!  *")
print("*    DEALER IS YOUR OPPONENT! PAY ATTENTION TO HIS HAND     *")
print("*#" * 30)

while playing:
    # create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the player's chips


    # prompt the Player for their Bet
    print(f"\nYou have {player_chips.balance} chips.")
    Chips.take_bet(player_chips)

    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # prompt for player fot hit or stand
        hit_or_stand(deck, player_hand)

        # show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # ife player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break
    # if player hasn't busted, play dealer's hand until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

            # show all cards
            show_all(player_hand, dealer_hand)

            # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()

    # inform player of their chips total
    print("\nyour total chips are {}".format(player_chips.balance))

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        if player_chips.balance == 0:
            print("\nYou do not have enough chips!")
            print("Thanks for playing! Bye")
            playing = False
        elif player_chips:
            playing = True
    else:
        print("Thanks for playing!")
        break
