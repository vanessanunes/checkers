from game.board import Board
from game.board import Piece
from game.player import Player

# if __name__ == "__main__":
if __name__ == "__main__":
    print('Lets create players?')

    nn = input('Digite seu nome:')
    cc = input('digite seu caracter')
    p1 = Player(nn, cc)
    
    nn = input('Digite seu nome:')
    cc = input('digite seu caracter')
    p2 = Player(nn, cc)
    
    print(p1, p2)

    # print(p1)
#     bb = Board(8, 8)
#     bb.setup()