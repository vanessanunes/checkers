class Player:
    """
    We can put player name, pieces chars, points and the quantity of pieces
    the players could do.
    """

    def __init__(self, name, char):
        self.name = name
        self.char = char
        self.pieces = None
        self.points = None

    # self.name = None
    #     # self.pieces_color = pieces_color
    #     self.points = points
    #     self.pieces = pieces

    def __str__(self):
        return('Return of player: "{}" with char "{}"'.format(self.name, self.char))
        # print('Player {} have {} point!'.format(self.name, self.points))

    def create_new(self):
        # import pdb
        # pdb.set_trace()
        self.name = input('Please, digit a new player: ')
        print(self.name)
        # self.char = input('Digit your char: ')
