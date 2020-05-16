import random
import time
deck = [
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
#INITIAL DEAL
total = 0
dealer_total = 0
card1 = deck.pop(random.randint(0, len(deck) - 1))
dealer_hidden = deck.pop(random.randint(0, len(deck) - 1))
card2 = 11 #deck.pop(random.randint(0, len(deck) - 1))
dealer_shown = deck.pop(random.randint(0, len(deck) - 1))
dealer_hand = [dealer_hidden, dealer_shown]
player_hand = [card1, card2]
print('Dealer:', dealer_shown)
print('Your Hand', player_hand)

#IF BLACKJACK
if 10 and 1 in player_hand and 10 and 1 not in dealer_hand:
    print('Black Jack!')
    quit()

#GAMEPLAY
while sum(player_hand) < 21 :
    time.sleep(1)
    hit = input('Hit or Stay? ')
    if hit == 'hit':
        time.sleep(1)
        dealt = deck.pop(random.randint(0, len(deck) - 1))
        print("Dealt:", dealt)
        player_hand.append(dealt)
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
    quit()
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
    quit()
#WHO WINS?
if sum(dealer_hand) == sum(player_hand) :
    print("Push")
elif sum(player_hand) > sum(dealer_hand) :
    print("You win!")
elif sum(dealer_hand) > sum(player_hand) :
    print('Dealer Wins!')

print('Your Hand:', player_hand, "=", sum(player_hand))
