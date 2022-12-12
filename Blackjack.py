
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



exit = False
lost = False
win = False

def deck_generator():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank,suit, values[rank]))
    return deck


def get_hand_total(hand):
    total = 0
    for i in hand:
        total = total + i[2]
    return total    


def pass_card(hand, deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


def show_hand(hand):
    for i in hand:
        print(i[0]+" of "+ i[1])
    total = get_hand_total(hand)
    print("Total: "+ str(total))  
    print()  




            






while exit == False:
    dealer_hand = []
    player_hand = []
    dealer_total = 0
    player_total = 0

    print("<<==========BLACKJACK==========>>\n")
    deck = deck_generator()
    pass_card(dealer_hand,deck)
    pass_card(player_hand,deck)
    pass_card(player_hand,deck)

   
    while True:
        print("\nYour Hand:")
        show_hand(player_hand)
        print("Dealer hand:")
        show_hand(dealer_hand)
        if get_hand_total(player_hand) > 21:
            print("You Busted!")
            break
        elif get_hand_total(player_hand) == 21:
            print("You win!")
            break
        
        else:
            hit_stand = input("Hit or Stand(H/S):")
            if hit_stand.lower() == 'h':
                pass_card(player_hand,deck)
                continue
            
            elif hit_stand.lower() == 's':
                while get_hand_total(dealer_hand) < 16:
                    pass_card(dealer_hand, deck)
                    print("\nYour Hand: ")
                    show_hand(player_hand)
                    print("Dealer Hand: ")
                    show_hand(dealer_hand)    

                if get_hand_total(dealer_hand) > 21:
                    print("Dealer Busted!")
                    break
                elif get_hand_total(dealer_hand) == 21:
                    print("Dealer Win!")
                    break
                elif get_hand_total(dealer_hand) < get_hand_total(player_hand):
                    print("You Win!")
                    break
                elif get_hand_total(dealer_hand) > get_hand_total(player_hand):
                    print("Dealer Win!")
                    break
                elif get_hand_total(dealer_hand) == get_hand_total(player_hand):
                    print("Tied")
                    break





    play_again=input("would like to play again?(Y/N)")
    if play_again.lower() == 'y':
        continue
    elif play_again.lower() == 'n':
        exit = True
    else:
        print('wrong option! Try again.')        
