
'''
Deck of cards and players
'''

import random as r
import Card_dict as c


class Player:
    
    # Holds all player data and their hand
    
    def __init__(self, name, deck, hs_i):
        
        # hs_i = handsize initial. Ie, for blackjack/texas hold 'em: 2, for 5 card draw: 5
        
        self._hs_i = hs_i
        
        self._name = name
        self._hand = Hand()
        
        # Which deck this player is using to draw from
        
        self._playdeck = deck
        self.initial(self.hs_i)
    
    def add(self, card):
        
        # Adds a specific card to hand
        
        self._hand.addCard(card)
        
    def hit(self):
        
        # Adds random card to hand from deck
        
        self._playdeck.deal(self)
        
    def drop(self, cardout):
        
        # Removes a specific card from hand
        
        self._hand.remCard(cardout)
        
    def swapHit(self, cardout):
        
        # Removes a specific card and adds a random one from the deck
        
        self.drop(cardout)
        self.hit()
        
    def swapCard(self, cardin, cardout):
        
        # Removes a specific card and adds a specific card
        
        self.drop(cardout)
        self.add(cardin)
        
    def initial(self, size):
        
        # Sets up initial hand based on hs_i
        
        for i in range(size):
            self.hit()
        
    def newhand(self):
        
        # Creates a new hand from the deck
        
        self._hand.Clear()
        self.initial()
        
    def printHand(self):
        
        # Prints the current content of the hand
        
        self._hand.printHand()
    
    def getName(self):
        
        # Returns the name of the player
        
        return self._name
    
    def getHand(self):
        
        # Returns the hand of the player
        
        return self._hand

class Card:
    
    # A class that contains data of a given card
    
    def __init__(self, val, suit):
        
        self._suit = suit            # Card's suit
        self._val = c.CardDict[val]  # Card's numeric value
        self._title = val + suit[0]  # Card's full title (shorthand)
        
    def AceSwitch(self):
        
        # Changes ace from high to low
        
        if(self._val == 11):
            self._val = 1
        elif(self._val == 1):
            self._val = 11
        
    def getTitle(self):
        
        # Gets the card's title
        
        return self._title
        
class Hand:
    
    def __init__(self):
        
        self._cards = []
        
    def addCard(self, card):
        
        # Adds a specific card to a hand
        
        self._cards.append(card)
        
    def remCard(self, card):
        
        # Removes a specific card from a hand
        
        self._cards.remove(card)
        
    def Clear(self):
        
        # Empties the hand
        
        self._cards = []
    
    def printHand(self):
        
        # Prints the hand in a scuffed but understandable format
        
        print('[', end = '')
        for i_card in self._cards:
            print(i_card.getTitle(), end = ", ")
        print(']')
    
    
class Deck:
    
    def __init__(self):
        
        self._cards = []
        self._reset()
        
    def deal(self, player):
        
        # Deals a specific player the topmost card on the deck
        
        card_out = self._cards[0]
        self._cards.pop(0)
        player.getHand.addCard(card_out)
        
    def shuffleDeck(self):
        
        # Shuffles the deck using random's shuffle function
        
        r.shuffle(self._cards)
        
    def reset(self):
        
        # Sets the deck back to a filled and randomized state
        
        self.cards = []

        for m_suit in c.SuitList:
            for m_card in c.CardList:
                self._cards.append(Card(m_card, m_suit))
                
        self.shuffleDeck()
    
    def printDeck(self):
        
        # Prints the deck in a scuffed but understandable manner
        
        print('[', end = '')
        for i_card in self._cards:
            print(i_card.getTitle(), end = ", ")
        print(']')
