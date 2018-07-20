suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('zero1','zero2','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

import random


class Card:
    '''
    Object to hold/set a cards attributes.
    '''
    suit = ''
    rank = ''
    def __init__(self,rank='Two',suit='Hearts'):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)
    
    def setSuit(self, suit):
        self.suit = suit
        
    def setRank(self, rank):
        self.rank = rank
    
    def getSuit(self):
        return (self.suit)
    
    def getRank(self):
        return self.rank
    
    def getValue(self):
        return values[self.rank]
    
    def get(self):
        return '{} of {}'.format(self.rank, self.suit)
    
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    '''
    Deck object. On initialize it should create a valid deck of 52 cards. 
    str returns current list of cards
    '''
    
    cards = []
    def __init__(self):
        self.cards = [Card() for i in range(52)]
        pointer = 0
        for x in range(len(suits)):
            for y in range(2,len(ranks)):
                self.cards[pointer].setRank(ranks[y])
                self.cards[pointer].setSuit(suits[x])
                pointer+=1
    
    def draw(self):
        #diagnostic print, omitted.
        #print('{} cards in the deck. drawing a card:'.format(len(self.cards)))
        drawn_number = random.randint(0,len(self.cards))
        #diagnostic print, omitted.
        #print('drawn number: {}'.format(str(drawn_number)))
        return self.cards.pop(drawn_number-1)
    
    def shuffle(self):
        random.shuffle(self.cards)

    
#cool way to check if cards are unique: len(list) == len(set(list))
#print('are all cards unique: '+str((len(self.cards) == len(set(self.cards)))))
    
    def __str__(self):
        output = 'current deck: \n'
        for x in range(len(self.cards)):
            output = output+str(x+1)+'. '+self.cards[x].get()+'\n'
        return output         
    
    

class Hand:
    '''
    Object that holds x cards. Can ADD to hand. Clears Hand. Returns attributes of Cards.
    Should return total value, if 21, over, or under. 
    '''
    cards = []
    def take(self,card):
        self.cards.append(card)
    
    def count(self):
        '''
        return the value total for the hand. check if player busts, if so, turn aces into 1's. 
        '''
        total = 0
        aces = 0
        for x in range(len(self.cards)):
            total = total + self.cards[x].getValue()
            if self.cards[x].getValue() == 11:
                aces+=1
        while total > 21 and aces > 0:
            total = total - 10
            aces = aces - 1
        return total
        
class Player(Hand):
    funds = 100
    def __init__(self,name='Player',start=100):
        self.funds = start
        self.name = name
        self.cards = []
    def getFunds(self):
        return self.funds
    def __str__(self):
        output = '{}\'s hand\n'.format(self.name)
        for x in range(len(self.cards)):
            output = output+str(x+1)+'. '+self.cards[x].get()+'\n'
        output = output + f'Total: {self.count()}'
        return output 


    