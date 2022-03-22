class Card():
    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'King', 'Queen']
    suits = []

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """

        :return: human readable string value of card
        """
        return self.rank + ' of ' + self.suit
        pass

    def __lt__(self, other):
        """

        :param other: other Card object
        :return: True/False if self > other
        """
        pass

    pass


class Deck():

    def __init__(self):
        """
        generate new deck of card
        """
        pass

    def shuffle(self):
        """

        :return: shuffled Deck object
        """
        pass

    def move_card(self, hand, number_of_card):
        """

        :param hand:
        :param number_of_card:
        :return:
        """

    pass


class Hand(Deck):
    pass


class Player():
    pass
