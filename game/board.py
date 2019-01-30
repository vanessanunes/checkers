"""
    define boards estructs
"""
# importar as coisas aqui


class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.height for i in range(self.width)]

    def __repr__(self):
        print(self.board)

    def setup(self):
        import pdb
        pdb.set_trace()

        # get line: self.board[0]
        # get column: self.board[0][2]


class Piece():

    def __init__(self, pieces):
        self.pieces = pieces

    def __repr__(self):
        return(
            'Quantities of pieces for any player is: {}\nOr, {} for all'
            .format(self.pieces, self.pieces * 2))

