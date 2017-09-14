class Value(object):

    def __init__(self, x = 0):
        self.val = x

    def __repr__(self):
        #return 'I am {}.'.format(self.val)
        return str(self.val)

    def set_val(self, x):
        self.val = x
    def get_val(self):
        return self.val
    def double_val(self):
        self.val += self.val
    

class Card(object):
    'card class'

    disp_ranks = {2: '2', 3: '3', 4: '4',5: '5',6: '6', 7: '7',
                  8: '8', 9: '9', 10: '10', 11: 'J',  12: 'Q',
                13: 'K',14: 'A'}
    disp_suits = {'C': 'C', 'S': 'S', 'H': 'H', 'D': 'D'}
    val_ranks = {2: 2, 3: 3, 4: 4,5: 5,6: 6, 7: 7,
                  8: 8, 9: 9, 10: 10, 11: 10,  12: 10,
                 13: 10, 14: 11}

    def __init__(self, rank = 2, suit = 'C'):
        self.set_rank(rank)
        self.set_suit(suit)

    
        
    def set_rank(self, rank):
        self.rk = rank

    def set_suit(self, suit):
        self.st = suit

    def display_card(self):
        return Card.disp_ranks[self.rk] + \
        Card.disp_suits[self.st]

    def __repr__(self):
        return self.display_card()


class frac(object):
    'fraction class, with addition and multiplication'

    def gcd(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return frac.gcd(b, a%b)

    def __init__(self, num, den):
        g = frac.gcd(num, den)
        self.n = num//g
        self.d = den//g

    def __repr__(self):
        #return '{}/{}'.format(self.n, self.d)
        return 'frac({}, {})'.\
               format(self.n, self.d)
        
    def __add__(self, other):
        a = self.n
        b = self.d
        c = other.n
        d = other.d
        e = a*d + b*c
        f = b*d
        return frac(e,f)

        
    def __mul__(self, other):
        a = self.n
        b = self.d
        c = other.n
        d = other.d
        e = a*c
        f = b*d
        return frac(e,f)

    


