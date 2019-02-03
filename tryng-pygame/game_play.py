from game import *

game = Game()
game.create_display()

# Game.teste()
"""
class Board():

    def __init__(self):
        self.gamers = ('x', 'o')
        self.board = [
            ['x', '-', 'x', '-', 'x', '-', 'x', '-']
            ['-', 'x', '-', 'x', '-', 'x', '-', 'x'],
            ['x', '-', 'x', '-', 'x', '-', 'x', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', 'o', '-', 'o', '-', 'o', '-', 'o'],
            ['o', '-', 'o', '-', 'o', '-', 'o', '-'],
            ['-', 'o', '-', 'o', '-', 'o', '-', 'o']
        ]


    def draw_board(_self):
        """
# Montar o tabuleiro
"""
        matriz = []

        for i in range(8):
            if i % 2 == 0:
                matriz.append(['#', '-', '#', '-', '#', '-', '#', '-'])
            else:
                matriz.append(['-', '#', '-', '#', '-', '#', '-', '#'])

            y = 0

            for i in range(len(matriz)):
                x = 0
                for c in range(len(matriz[1])):
                    if matriz[l][c] == '#':
                        pygame.draw.rect(display, board_color, (x, y, 75, 75))
                    else:
                        pygame.draw.rect(display, white_color, (x, y, 75, 75))
                    x += 75
                y += 75



    def loop_game():
        quit_game = False
        game = Game()

        while quit_game is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            display.fill(black_pieces)
            # game.draw_board()

            pygame.display.update()
            clock.tick(160)

# pygame.quit()
# quit()
"""
