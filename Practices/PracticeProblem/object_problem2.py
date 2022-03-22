import random


class Card():
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        self.rank = self.rank_names[rank]
        self.suit = self.suit_names[suit]

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __lt__(self, other):
        self_tuple = self.suit, self.rank
        other_tuple = other.suit, other.rank
        return self_tuple < other_tuple


class Deck():
    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def __str__(self):
        result = []
        for card in self.cards:
            result.append(str(card))
        return '\n'.join(result)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def move_cards(self, hand, number_of_cards):
        for i in range(number_of_cards):
            hand.add_card(self.pop_card())

    def deal_hands(self, number_of_hands, number_of_cards):
        hand_list = []
        for index1 in range(number_of_hands):
            hand_list.append(Hand())
        for hand in hand_list:
            self.move_cards(hand, number_of_cards)
        return hand_list


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == '__main__':
    # card1 = Card(1, 1)
    # print(card1)

    deck = Deck()
    deck.shuffle()
    # martin_hand = Hand('Martin')
    # deck.move_cards(martin_hand, 2)
    # print(martin_hand)

    hand_list = deck.deal_hands(3, 2)
    for hand in hand_list:
        print(hand)