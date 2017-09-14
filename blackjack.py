from random import shuffle

#global variables for presentation/valuation
ranks = [2,3,4,5,6,7,8,9,10,11,12,13,14]
disp_ranks = {2: '2', 3: '3', 4: '4',5: '5',6: '6', 7: '7',
                  8: '8', 9: '9', 10: '10', 11: 'J',  12: 'Q',
                13: 'K',14: 'A'}

suits = ['C', 'S', 'H', 'D']
disp_suits = {'C': 'C', 'S': 'S', 'H': 'H', 'D': 'D'}

val_ranks = {2: 2, 3: 3, 4: 4,5: 5,6: 6, 7: 7,
                  8: 8, 9: 9, 10: 10, 11: 10,  12: 10,
                13: 10,14: 11}
#cards

def init_card(rank, suit):
    'create card with rank and suit'
    return (rank, suit)

def rank_card(c):
    'return rank of card'
    return c[0]

def suit_card(c):
    'return suit of card'
    return c[1]

#def display_card(c):
#    return disp_ranks[c[0]] + disp_suits[c[1]]
    
def display_card(c):
    'return nice string presentation of card'
    rank = rank_card(c)
    suit = suit_card(c)
    return disp_ranks[rank] + disp_suits[suit]

def score_card(c):
    'score of card'
    rank = rank_card(c)
    return val_ranks[rank]

#deck

def add_card(card, deck):
    'add card to deck or hand'
    deck.append(card)

def init_deck():
    'create inital deck'
    deck = []
    for r in ranks:
        for s in suits:
            card = init_card(r,s)
            add_card(card, deck)
    return deck

def deal_card(deck):
    'deal a card of deck and return it'
    return deck.pop()

def shuffle_deck(deck):
    'shuffle deck'
    shuffle(deck)

#hand
    
def init_hand():
    'create empty hand'
    hand = []
    return hand

def show_hand(hand):
    'create nice string presentation of hand'
    s = ''
    if len(hand) == 0:
        return ''
    for card in hand:
        s += display_card(card) + ', '
    return s[:-2]

def num_cards(hand):
    'return size of hand'
    return len(hand)

def compare_hands(h1, h2):
    '0: h1 wins, 1: h2 wins, 2: tie'

    if score_hand(h1) < score_hand(h2):
        return 1
    elif score_hand(h2) < score_hand(h1):
        return 0
    else: #score_hand(h1) == score_hand(h2)
        if score_hand(h1) == 21:
            if num_cards(h1) == 2 and num_cards(h2) > 2:
                return 0
            elif num_cards(h2) == 2 and num_cards(h1) > 2:
                return 1
            else:
                return 2
        else:
            return 2

    
def score_hand(hand):
    'score hand, including soft aces'
    
    val = 0
    for card in hand:
        val += score_card(card)
    num_aces = 0
    for card in hand:
        if rank_card(card) == 14:
            num_aces += 1
    #as long as there are hard aces, and the score is > 21, make them soft
    while (val > 21 and num_aces > 0):
        val -= 10
        num_aces -= 1
    return val


def blackjack():
    'play the game of blackjack'

    deck = init_deck()
    shuffle_deck(deck)
    
    handP = init_hand()
    handH = init_hand()

    for i in range(2):
        card = deal_card(deck)
        add_card(card, handP)
    for i in range(2):
        card = deal_card(deck)
        add_card(card, handH)

    while(True):
        print('Player\'s hand: {}'.\
              format(show_hand(handP)))
        if score_hand(handP) > 21:
            print('You lose.')
            return
        dec = input('(H)it or (S)tand: ')
        if dec.lower()[0] == 'h':
            card = deal_card(deck)
            add_card(card, handP)
        else:
            break

    while(True):
        print('House hand: {}'.\
              format(show_hand(handH)))
        if score_hand(handH) > 21:
            print('The House loses.')
            return
        if score_hand(handH) < 17:
            print('The house takes a card.')
            card = deal_card(deck)
            add_card(card, handH)
        else:
            print('The house stands.')
            break    

    if compare_hands(handP, handH) == 0:
        print('The player wins.')
    elif compare_hands(handP, handH) == 1:
        print('The house winds.')
    else:
        print('It\'s a tie.')
        
