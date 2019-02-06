class Player:
    """
    We can put player name, pieces chars, points and the quantity of pieces
    the players could do.
    """

    def __init__(self, name, char):
        self.name = name
        self.char = char
        self.points = 0

    def __str__(self):
        return '{}'.format(self.name)
