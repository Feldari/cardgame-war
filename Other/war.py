#!/usr/bin/env python3.6

import random


def init():
    '''
    This builds the deck to draw from.
    This runs at the beginning of the program then shoud only be run
    to start a new game.
    '''

    # These are the possible face values and suits for the cards.
    cardfaces = ("A","K","Q","J","10","9","8","7","6","5","4","3","2")
    cardsuits = ("H","S","D","C")

    # This section builds the cards with their assigned suits
    # ex. thisdeck = [AH, KH, QH, ...]
    thisdeck = []
    complete_deck = []
    for suit in cardsuits:
        for face in cardfaces:
            thisdeck.append(face+suit)

    # This section takes the completed deck and assigns each card to a tuple
    # This tuple has the generated card value and suit at complete_deck[*]
    # The card's numeric stregnth is stored in complete_deck[*][*]
    # A = 14, K = 13, Q = 12, J = 11
    # ex. complete_deck = [(AH, 14), (KH, 13), (QH, 12), ... ]
    for card in thisdeck:
        card_value = ''
        for value in card:
            if value == 'D' or value == 'S' or value == 'C' or value == 'H':
                break
            elif value == 'A' or value == 'K' or value == 'Q' or value == 'J':
                if value == 'A':
                    card_value = 14
                elif value == 'K':
                    card_value = 13
                elif value == 'Q':
                    card_value = 12
                else:
                    card_value = 11
            else:
                card_value = card_value + str(value)
        complete_deck.append((card, int(card_value)))

    return complete_deck


def shuffle(mycards):
    '''
    This takes the input list and shuffles it. 
    In war.py it is used to shuffle decks of cards stord in lists.
    Requires import random.
    '''
    unshuffled = mycards
    shuffled = []
    for count in range (0,len(unshuffled)):
        pick = ''
        while (pick == ''):
            pick = random.choice(unshuffled)
            shuffled.append(pick)
            unshuffled.remove(pick)
    return shuffled


def startinghands(deck):
    '''
    This function divides the availible cards to the two players.
    '''
    hand0 = []
    hand1 = []
    count = 0

    for deal in range(0,len(deck)):
        # Switch the target player when dealing each card.
        # This reflects a real card deal.
        if count % 2 == 0:
            hand0.append(deck[deal])
        else:
            hand1.append(deck[deal])
        # instead of .append() I may want to use insert to place new cards at
        # the front of the list. This would reflect a real deal even closer.
        count += 1
    return (hand0, hand1)


def print_hands(p1hand, p2hand):
    '''
    This prints the current hands for the players.
    It only prints the face value and suit.
    It does not print the converted value for the card.
    '''
    print ('Player 1 has', len(p1hand), 'card(s): ')
    for card_pair in p1hand:
        print (card_pair[0], end=' ')
    print('\n')

    print ('Player 2 has', len(p2hand), 'card(s): ')
    for card_pair in p2hand:
        print (card_pair[0], end=' ')
    print('\n')


def fight(hand1, hand2):
    '''
    This function is the core for comparing the cards
    The function expects 2 lists of tuples containing the players hands.
    example input: [(AH, 14), (KH, 13), (QH, 12), ... ]
    '''
    card1 = ''
    card2 = ''
    player1loot = []
    player2loot = []

    while hand1 != [] and hand2 != []:

        while hand1 != [] and hand2 != []:
            
            print ()
            print ('Card pair: ')
            print ('Player 1: ', hand1[0][0])
            print ('Player 2: ', hand2[0][0])

            # #################################
            # #######TO DO#####################
            if hand1[0][0] == hand2[0][0]:
                # war(hand1, hand2, player1loot, player2loot)
                hand1.pop(0)
                hand2.pop(0)
            # #####COMPLETE WAR FUNCTION ABOVE#
            # #################################
            
            elif hand1 > hand2:
                print ('Player 1 wins hand')
                player1loot.append(hand1[0])
                player1loot.append(hand2[0])
                hand1.pop(0)
                hand2.pop(0)

            else:
                print ('Player 2 wins hand')
                player2loot.append(hand1[0])
                player2loot.append(hand2[0])
                hand1.pop(0)
                hand2.pop(0)

        '''    
        # uncomment below lines to see how cards move during shuffling process
        # see below comment block too!
        print ('-------------------Before Shuffle-------------------')
        print ('\#cards', len(hand1), 'hand1', hand1)
        print ('\#cards', len(hand2), 'hand2', hand2)
        print ()
        print ('\#cards', len(player1loot), 'p1loot', player1loot)
        print ('\#cards', len(player2loot), 'p2loot', player2loot)
        print ()
        # uncomment above lines to see how cards move during shuffling process
        ''' 

        # ??????Why does this blank the list used for the argument???
        if hand1 == []:
            print('Shuffling player 1\'s hand')
            hand1 = shuffle(player1loot)
        else:
            pass

        if hand2 == []:
            print('Shuffling player 2\'s hand')
            hand2 = shuffle(player2loot)
        else:
            pass

        
        '''
        # uncomment below lines to see how cards move during shuffling process
        # see above comment block too!
        print ('-------------------After Shuffle--------------------')
        print ('\#cards', len(hand1), 'hand1', hand1)
        print ('\#cards', len(hand2), 'hand2', hand2)
        print ()
        print ('\#cards', len(player1loot), 'p1loot', player1loot)
        print ('\#cards', len(player2loot), 'p2loot', player2loot)
        print ()
        # uncomment above lines to see how cards move during shuffling process
        '''


        # check to see if player hand is still empty after shuffle
        # if it is other player wins!!

        if hand1 == []:
            print ('Player 2 Wins!!')
        else:
            pass
        
        if hand2 == []:
            print ('Player 1 Wins!!')
        else:
            pass


def war(hand1, hand2, player1loot, player2loot):
    '''
    If two cards match in the war function this one resolves the tie.
    '''
    print ('WAR!!!')
    print ('P1 card: ', hand1[0][0], 'P2 card: ', hand2[0][0])
    print ('Cards on the line: ')
    print ('          P1           P2')
    for card in range(3):
        print ('         ', hand1[card][0], hand2[card][0]
    


if __name__ == '__main__':
    # These lines start the game and initialize the deck and player's hands.
    cards = init()
    cards = shuffle(cards)
    cards = startinghands(cards)
    p1hand = cards[0] 
    p2hand = cards[1] 
    # ######################################################################

    # This will print the players starting hands.
    print_hands(p1hand, p2hand)


    fight(p1hand, p2hand)

