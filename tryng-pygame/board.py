import pygame
from players import *


class Board():

    selected_index = None
    shift = 1
    jumping = False

    players = ('x', 'o')
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    red_color = (225, 60, 60)
    light_red_color = (231, 98, 98)
    light_green_color = (111, 201, 112)
    # board_color = (141,117,86)
    # board_color = (177,147,108)
    board_color = (159, 132, 97)
    pygame.font.init()

    height = 600
    width = 800

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
                    pygame.draw.rect(board, self.board_color,
                                     pygame.Rect([x, y, 75, 75]))
                else:
                    pygame.draw.rect(board, self.white_color, [x, y, 75, 75])
                x += 75
            y += 75
        self.draw_pieces(board)

        # selected_index
        if self.selected_index:
            required = self.all_moves()
            movs = self.possibles_moves(self.selected_index)

            if required != {}:
                if (self.selected_index[0], self.selected_index[1]) not in required:
                    x_red = self.height / 8 * self.selected_index
                    y_red = self.height / 8 * self.selected_index

                    pygame.draw.react(
                        board, self.light_red_color, (x_red, y_red), 75, 75)

                else:
                    if movs[0] == []:
                        x_red = self.height / 8 * self.selected_index[1]
                        y_red = self.height / 8 * self.selected_index[0]

                        pygame.draw.rect(
                            board, self.light_green_color, (x_red, y_red), 75, 75)
                    else:
                        for i in range(len(movs[0])):
                            x_possible = self.height / 8 * movs[0][i][1]
                            y_possible = self.height / 8 * movs[0][i][0]

                            pygame.draw.rect(
                                board, self.light_green_color, (x_possible, y_possible, 75, 75))

            else:
                if self.moving:
                    x_red = self.height / 8 * self.selected_index[1]
                    y_red = self.height / 8 * self.selected_index[0]

                    pygame.draw.rect(board, self.light_red_color,
                                     (x_red, y_red), 75, 75)
                else:
                    if movs[0] == []:
                        x_red = self.height / 8 * self.selected_index[1]
                        y_red = self.height / 8 * self.selected_index[0]

                        pygame.draw.rect(
                            board, self.light_green_color, (x_red, y_red), 75, 75)
                    else:
                        for i in (range(len(movs[0]))):
                            x_possible = self.height / 8 * movs[0][i][1]
                            x_possible = self.height / 8 * movs[0][i][0]

                            pygame.draw.rect(
                                board, self.light_green_color, (x_possible, y_possible), 75, 75)

        self.draw_pieces(board)
        # import pdb
        # pdb.set_trace()

        pygame.display.flip()
        # self.move_capt
        # self.play(board)

    def draw_pieces(self, board):
        """
            draw all the starter pieces in the board
        """
        for l in range(len(self.matriz_players)):
            for c in range(len(self.matriz_players[l])):
                element = self.matriz_players[l][c]

                if element != '-':
                    x = int(self.height / 8 * c + self.height / 16)
                    y = int(self.height / 8 * l + self.height / 16)

                    if element.lower() == 'x':
                        pygame.draw.circle(
                            board, self.red_color, [x, y], 20, 0)
                        if element == 'X':
                            pygame.draw.circle(
                                board, self.black_color, (x, y), 10, 0)
                            pygame.draw.circle(
                                board, self.blue_color, (x, y), 5, 0)
                    else:
                        pygame.draw.circle(
                            board, self.white_color, (x, y), 20, 0)
                        if element == 'O':
                            pygame.draw.circle(
                                board, self.black_color, (x, y), 10, 0)
                            pygame.draw.circle(
                                board, self.blue_color, (x, y), 5, 0)

        font = pygame.font.Font(None, 20)

        x = sum([cont.count('x') + cont.count('X')
                 for cont in self.matriz_players])
        o = sum([cont.count('o') + cont.count('O')
                 for cont in self.matriz_players])

    def avalia_clique(self, pos):
        shift = self.shift % 2
        # if self.status == "Jogando":
        line, column = self.clicked_line(pos), self.clicked_column(pos)
        if self.selected_index:
            movs = self.is_movs_valido(
                self.players[shift], self.selected_index, line, column)
            if movs[0]:
                self.jogar(
                    self.players[shift], self.selected_index, line, column, movs[1])
            elif line == self.selected_index[0] and column == self.selected_index[1]:
                movs = self.required_moves(self.selected_index)
                if movs[0] == []:
                    if self.jumps:
                        self.jumps = False
                        self.next_shift()
                self.selected_index = None
        else:
            if self.matriz_players[line][column].lower() == self.players[shift]:
                self.selected_index = [line, column]

    def next_shift(self):
        self.shift += 1

    def clicked_line(self, pos):
        y = pos[1]
        for i in range(1, 8):
            if y < i * self.height / 8:
                return i - 1
        return 7

    def clicked_column(self, pos):
        x = pos[0]
        for i in range(1, 8):
            if x < i * self.height / 8:
                return i - 1
        return 7

    def play(self, board):
        # cedula selecionada == selectes index
        atual = self.matriz_players[2][0]
        prox = self.matriz_players[3][1]

        self.matriz_players[2][0] = prox
        self.matriz_players[3][1] = atual
        # self.matriz_players[2][]

    # game over
    def status_gameover(self):
        pass

    # todos_required
    def all_moves(self):
        all = {}

        for r in range(len(self.matriz_players)):
            for c in range(len(self.matriz_players[r])):
                om, moves = self.possibles_moves((r, c))
                if om != []:
                    all[(r, c)] = om

        return all

    # existe_possivel
    def NOME_A_DEFINIR(self):
        """
        Returns if a move is possible
        """
        for l in range(len(self.matriz_players)):
            for c in range(len(self.matriz_players[1])):
                if self.possibles_moves((l, c)):
                    return True

        return False

    # moves_possiveis
    # moves_possiveis
    def possibles_moves(self, index):
        moves, jumps = self.required_moves(index)

        if moves == []:
            line = index[0]
            column = index[1]

            if self.matriz_players[line][column].islower():
                if self.matriz_players[line][column] == 'o':
                    if line > 0:
                        if column < 7:
                            if self.matriz_players[line - 1][column + 1] == '-':
                                moves.append([line - 1, column + 1])
                        if column > 0:
                            if self.matriz_players[line - 1][column - 1] == '-':
                                moves.append([line - 1, column - 1])

                elif self.matriz_players[line][column] == 'x':
                    if line < 7:
                        if column < 7:
                            if self.matriz_players[line + 1][column + 1] == '-':
                                moves.append([line + 1, column + 1])
                        if column > 0:
                            if self.matriz_players[line + 1][column - 1] == '-':
                                moves.append([line + 1, column - 1])
            elif self.matriz_players[line][column].isupper():
                count_line = line
                count_column = column
                while True:
                    if count_line - 1 < 0 or count_column - 1 < 0:
                        break
                    else:
                        if self.matriz_players[count_line - 1][count_column - 1] == '-':
                            moves.append([count_line - 1, count_column - 1])
                        else:
                            break
                    count_line -= 1
                    count_column -= 1

                count_line = line
                count_column = column
                while True:
                    if count_line - 1 < 0 or count_column + 1 > 7:
                        break
                    else:
                        if self.matriz_players[count_line - 1][count_column + 1] == '-':
                            moves.append([count_line - 1, count_column + 1])
                        else:
                            break
                    count_line -= 1
                    count_column += 1

                count_line = line
                count_column = column
                while True:
                    if count_line + 1 > 7 or count_column + 1 > 7:
                        break
                    else:
                        if self.matriz_players[count_line + 1][count_column + 1] == '-':
                            moves.append([count_line + 1, count_column + 1])
                        else:
                            break
                    count_line += 1
                    count_column += 1

                count_line = line
                count_column = column
                while True:
                    if count_line + 1 > 7 or count_column - 1 < 0:
                        break
                    else:
                        if self.matriz_players[count_line + 1][count_column - 1] == '-':
                            moves.append([count_line + 1, count_column - 1])
                        else:
                            break
                    count_line += 1
                    count_column -= 1
        return moves, jumps

    # movs_obrigatorio
    def required_moves(self, index):
        """
        Show the moves that's possible to do
        """
        required = []
        new_position = []

        l = index[0]
        c = index[1]

        # COMO SABER QUAL JOGADOR
        player = self.players[self.shift % 2]
        index = self.players.index(player)

        array = [player.lower(), player.upper(), '-']

        if self.matriz_players[l][c].islower() and self.matriz_players[l][c] == player and self.shift % 2 == index:
            if l > 0:
                if c < 7:
                    if self.matriz_players[l - 1][c + 1].lower() not in array:
                        l_x = l + 1
                        l_c = c + 1
                        if l_x - 1 >= 0 and l_c + 1 <= 7:
                            if self.matriz_players[l_x - 1][l_c + 1] == '-':
                                required.append([l_x - 1, l_c + 1])
                                new_position.append((l_x, l_c))
                    if c > 0:
                        if self.matriz_players[l - 1][c - 1].lower() not in array:
                            l_x = l - 1
                            l_c = c - 1

                            if l_x - 1 >= 0 and l_c - 1 >= 0:
                                if self.matriz_players[l_x - 1][l_c - 1] == '-':
                                    required.append([l_x - 1, l_c - 1])
                                    new_position.append((l_x, l_c))
                if l < 7:
                    if c < 7:
                        if self.matriz_players[l + 1][c + 1].lower() not in array:
                            l_x = l + 1
                            l_c = c + 1

                            if l_x + 1 <= 7 and l_c + 1 <= 7:
                                if self.matriz_players[l_x + 1][l_c + 1] == '-':
                                    required.append([l_x + 1, l_c + 1])
                                    new_position.append((l_x, l_c))
                    if c > 0:
                        if self.matriz_players[l + 1][c - 1].lower() not in array:
                            l_x = l + 1
                            l_c = c - 1

                            if l_x + 1 <= 7 and l_c - 1 >= 0:
                                if self.matriz_players[l_x + 1][l_c - 1] == '-':
                                    required.append([l_x + 1, l_c - 1])
                                    new_position.append((l_x, l_c))

        elif self.matriz_players[l][c].isupper() and self.matriz_players[l][c] == jogador.upper() and self.turno % 2 == index:

            if not self.jumping and (jogador.lower() == 'x' and l != 7) or (jogador.lower() == 'o' and l != 0):
                count_line = l
                count_column = c
                while True:
                    if count_line - 1 < 0 or count_column - 1 < 0:
                        break
                    else:
                        if self.matriz_players[count_line - 1][count_column - 1] not in array:
                            l_x = count_line - 1
                            l_c = count_column - 1

                            if l_x - 1 >= 0 and l_c - 1 >= 0:
                                if self.matriz_players[l_x - 1][l_c - 1] == '-':
                                    new_position.append((l_x, l_c))
                                    while True:
                                        if l_x - 1 < 0 or l_c - 1 < 0:
                                            break
                                        else:
                                            if self.matriz_players[l_x - 1][l_c - 1] == '-':
                                                required.append(
                                                    [l_x - 1, l_c - 1])
                                            else:
                                                break
                                        l_x -= 1
                                        l_c -= 1
                            break
                    count_line -= 1
                    count_column -= 1

                count_line = l
                count_column = c
                while True:
                    if count_line - 1 < 0 or count_column + 1 > 7:
                        break
                    else:
                        if self.matriz_players[count_line - 1][count_column + 1] not in array:
                            l_x = count_line - 1
                            l_c = count_column + 1

                            if l_x - 1 >= 0 and l_c + 1 <= 7:
                                if self.matriz_players[l_x - 1][l_c + 1] == '-':
                                    new_position.append((l_x, l_c))
                                    while True:
                                        if l_x - 1 < 0 or l_c + 1 > 7:
                                            break
                                        else:
                                            if self.matriz_players[l_x - 1][l_c + 1] == '-':
                                                required.append(
                                                    [l_x - 1, l_c + 1])
                                            else:
                                                break
                                        l_x -= 1
                                        l_c += 1
                            break
                    count_line -= 1
                    count_column += 1

                count_line = l
                count_column = c
                while True:
                    if count_line + 1 > 7 or count_column + 1 > 7:
                        break
                    else:
                        if self.matriz_players[count_line + 1][count_column + 1] not in array:
                            l_x = count_line + 1
                            l_c = count_column + 1

                            if l_x + 1 <= 7 and l_c + 1 <= 7:
                                if self.matriz_players[l_x + 1][l_c + 1] == '-':
                                    new_position.append((l_x, l_c))
                                    while True:
                                        if l_x + 1 > 7 or l_c + 1 > 7:
                                            break
                                        else:
                                            if self.matriz_players[l_x + 1][l_c + 1] == '-':
                                                required.append(
                                                    [l_x + 1, l_c + 1])
                                            else:
                                                break
                                        l_x += 1
                                        l_c += 1
                            break
                    count_line += 1
                    count_column += 1

                count_line = l
                count_column = c
                while True:
                    if count_line + 1 > 7 or count_column - 1 < 0:
                        break
                    else:
                        if self.matriz_players[count_line + 1][count_column - 1] not in array:
                            l_x = count_line + 1
                            l_c = count_column - 1

                            if l_x + 1 <= 7 and l_c - 1 >= 0:
                                if self.matriz_players[l_x + 1][l_c - 1] == '-':
                                    new_position.append((l_x, l_c))
                                    while True:
                                        if l_x + 1 > 7 or l_c - 1 < 0:
                                            break
                                        else:
                                            if self.matriz_players[l_x + 1][l_c - 1] == '-':
                                                required.append(
                                                    [l_x + 1, l_c - 1])
                                            else:
                                                break
                                        l_x += 1
                                        l_c -= 1
                            break
                    count_line += 1
                    count_column -= 1

        return required, new_position

    # move_is_valid
    def move_is_valid(self):
        original_line = localizacao_cedula[0]
        original_column = localizacao_cedula[1]

        obrigatorios = self.todos_obrigatorios()

        if obrigatorios != {}:
            if (original_line, original_column) not in obrigatorios:
                return False, None
            elif [destiny_line, destiny_column] not in obrigatorios[(original_line, original_column)]:
                return False, None

        movs, jump = self.movss_possiveis(localizacao_cedula)

        if [destiny_line, destiny_column] in movs:
            if jump:
                if len(jump) == 1:
                    return True, jump[0]
                else:
                    for i in range(len(jump)):
                        if abs(jump[i][0] - destiny_line) == 1 and abs(jump[i][1] - destiny_column) == 1:
                            return True, jump[i]

            if self.jumping:
                return False, None

            return True, None

return False, None

