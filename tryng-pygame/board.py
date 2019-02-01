import pygame

class Board():

    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    red_color = (225, 60, 60)
    # board_color = (141,117,86)
    # board_color = (177,147,108)
    board_color = (159, 132, 97)
    pygame.font.init()


    heigth = 800
    width = 600

    matriz_players = [
        ['x', '-', 'x', '-', 'x', '-', 'x', '-'],
        ['-', 'x', '-', 'x', '-', 'x', '-', 'x'],
        ['x', '-', 'x', '-', 'x', '-', 'x', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'o', '-', 'o', '-', 'o', '-', 'o'],
        ['o', '-', 'o', '-', 'o', '-', 'o', '-'],
        ['-', 'o', '-', 'o', '-', 'o', '-', 'o']]

    def draw_board(self, board):
        """
            draw board
        """
        matriz = []

        for i in range(8):
            if i % 2 == 0:
                matriz.append(['#', '-', '#', '-', '#', '-', '#', '-'])
            else:
                matriz.append(['-', '#', '-', '#', '-', '#', '-', '#'])

        y = 0
        for l in range(len(matriz)):
            x = 0
            for c in range(len(matriz[l])):
                if matriz[l][c] == '#':
                    pygame.draw.rect(board, self.board_color, pygame.Rect([x, y, 75, 75]))
                else:
                    pygame.draw.rect(board, self.white_color, [x, y, 75, 75])
                x += 75
            y += 75
        # pygame.display.flip()
        self.draw_pieces(board)

    def draw_pieces(self, board):
        # BUILDING HERE
        for l in range(len(self.matriz_players)):
            for c in range(len(self.matriz_players[l])):
                element = self.matriz_players[l][c]
                # import pdb
                # pdb.set_trace()
                if element != '-':
                    x = int(self.heigth / 8 * c + self.heigth / 16)
                    y = int(self.heigth / 8 * 1 + self.heigth / 16)
                    import pdb
                    pdb.set_trace()
                    if element.lower() == 'x':
                        # print(x, y)
                        pygame.draw.circle(board, self.red_color, [x, y], 20, 0)
                        if element == 'X':
                            pygame.draw.circle(board, self.black_color, (x, y), 10, 0)
                            pygame.draw.circle(board, self.blue_color, (x, y), 5, 0)
                    else:
                        pygame.draw.circle(board, self.white_color, (x, y), 20, 0)
                    if element == 'O':
                        pygame.draw.circle(board, self.black_color, (x, y), 10, 0)
                        pygame.draw.circle(board, self.blue_color, (x, y), 5, 0)

        font = pygame.font.Font(None, 20)

        x = sum([cont.count('x') + cont.count('X') for cont in self.matriz_players])
        o = sum([cont.count('o') + cont.count('O') for cont in self.matriz_players])
        print(x, o)
        pygame.display.flip()

            # print(l)
        

        
        # if self.cedula.selecionada
