#This seems to be working 5/16/2020
import random
import time
import copy
deckinit = [
2,2,2,2,
3,3,3,3,
4,4,4,4,
5,5,5,5,
6,6,6,6,
7,7,7,7,
8,8,8,8,
9,9,9,9,
10,10,10,10,
10,10,10,10,
10,10,10,10,
10,10,10,10,
11,11,11,11,
]
purse = 100
decks = copy.copy(deckinit)
def single_deal(deck) :
    #INITIAL DEAL
    global purse
    total = 0
    dealer_total = 0
    print("Purse:", purse)
    while True :
        print("How much is your bet?")
        bet = input()
        bet = int(bet)
        if bet > purse or bet <= 0 :
            print('You can only bet up to your purse total\nYour purse is', purse)
        else:
            break
    purse -= bet
    card1 = deck.pop(random.randint(0, len(deck) - 1))
    dealer_hidden = deck.pop(random.randint(0, len(deck) - 1))
    card2 = deck.pop(random.randint(0, len(deck) - 1))
    dealer_shown = deck.pop(random.randint(0, len(deck) - 1))
    dealer_hand = [dealer_hidden, dealer_shown]
    player_hand = [card1, card2]
    print('Dealer: [  '+ str(dealer_shown) +']')
    print('Your Hand:', player_hand)

    #IF BLACKJACK
    if 10 in player_hand and 11 in player_hand and 11 not in dealer_hand :
        time.sleep(1)
        print('Dealer Hand: ', dealer_hand)
        time.sleep(1)
        print('Black Jack!')
        time.sleep(1)
        purse += bet * 2
        return
    # insurance
    if dealer_shown == 11:
        print('Would you like to buy insurance?')
        ins = input()
        if 'y' in ins and dealer_hidden == 10:
            print('Insurance Bet:', bet/2)
            time.sleep(1)
            print('Dealer Hand:', dealer_hand)
            purse += bet
            return
        elif 'y' in ins :
            print('Insurance Bet:', bet/2)
            purse -= bet/2
            print('Purse:', purse)

    #GAMEPLAY
    while sum(player_hand) <= 21 :
        time.sleep(1)
        hit = input('Hit or Stay? ')
        if 'h' in hit:
            time.sleep(1)
            dealt = deck.pop(random.randint(0, len(deck) - 1))
            print("Dealt:", dealt)
            player_hand.append(dealt)
            print('Your Hand:', player_hand)
            if 11 in player_hand and sum(player_hand) > 21:
                Ace = player_hand.index(11)
                player_hand.remove(11)
                player_hand.insert(Ace, 1)
                print('Your Hand:', player_hand)
            continue
        else:
            break

    #IF PLAYER BUSTS
    if sum(player_hand) > 21 :
        print("Bust! You Lose!")
        return
    print("Dealer:", dealer_hand)
    time.sleep(1)

    #DEALERS TURN
    while sum(dealer_hand) < 17 :
        dealer_card = deck.pop(random.randint(0, len(deck) - 1))
        dealer_hand.append(dealer_card)
        print('Dealer Hits:', dealer_card)
        time.sleep(1)
        print('Dealer Hand:',dealer_hand, "=", sum(dealer_hand))
        time.sleep(1)
    #DEALER BUSTS
    if sum(dealer_hand) > 21:
        print("Dealer Busts! You Win!")
        purse += bet * 2
        return
    #WHO WINS?
    if sum(dealer_hand) == sum(player_hand) :
        print("Push")
        return
    elif sum(player_hand) > sum(dealer_hand) :
        print("You win!")
        purse += bet *2
        return
    elif sum(dealer_hand) > sum(player_hand) :
        print('Dealer Wins!')
        return
    print('Your Hand:', player_hand, "=", sum(player_hand))
single_deal(decks)
print("Purse:",purse)
print('Play again?')
again = input('y/n')
while again == 'y' :
    single_deal(decks)
    decks = copy.copy(deckinit)
    print("Purse:",purse)
    print('Play again?')
    again = input('y/n: ')
quit()
