from .piece import Piece

class Player:
    """
    We can put player name, pieces chars, points and the quantity of pieces
    the players could do.
    """

    def __init__(self, name, char):
        self.name = name
        self.char = Piece(char)
        self.points = 0

    def __str__(self):
        return('Return of player: "{}" with char "{}"'.format(
            self.name, self.char))
        # print('Player {} have {} point!'.format(self.name, self.points))
