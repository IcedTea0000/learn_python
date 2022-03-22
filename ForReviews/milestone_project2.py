from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12,
                  "King": 13, "Ace": 14}
        self.value = values[rank]

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = []

    def generate_new_deck(self):
        for suit in ("Clubs", "Spades", "Hearts", "Diamonds"):
            for rank in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"):
                card = Card(suit=suit, rank=rank)
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            print(card, end="| ")
        print()

    def shuffle(self, times):
        try:
            if int(times) < 0:
                raise Exception("times must be positive number")
        except ValueError:
            print("times must be number")
        else:
            for time in range(0, times):
                shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"Player {self.name} has {len(self.hand)} card"

    def remove_one(self):
        return self.hand.pop(0)

    def add_cards(self, cards):
        if type(cards) == type(self.hand):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)


def game_play():
    game_on = True
    round_num = 1
    player1 = Player(name="Player1")
    player2 = Player(name="Player2")
    deck = Deck()
    deck.generate_new_deck()
    deck.shuffle(3)
    for index in range(26):
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())

    # print(player1)
    # print(player2)

    while game_on:
        # split card to player
        if len(player1.hand) == 0:
            print("Player 1 wins")
            break
        elif len(player2.hand) == 0:
            print("Player 2 wins")
            break

        player1_cards = []
        player1_cards.append(player1.remove_one())
        player2_cards = []
        player2_cards.append(player2.remove_one())

        at_war = True
        while at_war:
            print("============ROUND {}============".format(round_num))
            round_num +=1
            if player1_cards[-1].value > player2_cards[-1].value:
                print("Player 1: {} > Player 2 : {}".format(player1_cards[-1], player2_cards[-1]))
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                at_war = False
            elif player1_cards[-1].value < player2_cards[-1].value:
                print("Player 1: {} < Player 2 : {}".format(player1_cards[-1], player2_cards[-1]))
                player2.add_cards(player2_cards)
                player2.add_cards(player1_cards)
                at_war = False
            else:
                print("WAR!")
                if len(player1.hand) < 3:
                    print("player 1 unable to declare war")
                    print("player 2 win")
                    game_on = False
                    break
                elif len(player2.hand) < 3:
                    print("player 2 unable to declare war")
                    print("player 1 win")
                    game_on = False
                    break
                else:
                    for index in range(3):
                        player1_cards.append(player1.remove_one())
                        player2_cards.append(player2.remove_one())


if __name__ == "__main__":
    game_play()
