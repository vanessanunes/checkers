# -*- coding: utf-8 -*-
from game.player import Player
from game.board import Board


class Game():
    board = Board()
    matriz = board.board
    players = [None, None]
    player = None
    score = {
        'x': 0,
        'o': 0,
    }
    shift = 0

    def __init__(self):
        print('\t ** Welcome to the Checkers Game! ** ')
        self.create_players()

    def start(self):
        self.board.show_matriz()
        self.round()

    def create_players(self):
        self.players[0] = Player('Player 1', 'o')
        self.players[1] = Player('Player 2', 'x')

    def define_player(self):
        if self.shift % 2 == 0:
            self.player = self.players[0]
        else:
            self.player = self.players[1]
        print('~> Player {} move the piece {}, shift {}'.format(
            str(self.player), self.player.char, self.shift + 1))

    def verify_move(self, casa_atual, casa_nova):
        atual_line, atual_col = self.detach_item(casa_atual)
        new_line, new_col = self.detach_item(casa_nova)

        if new_line == atual_line or atual_col == new_col:
            print('!!! WRONG MOVE !!! Try again')
            return False

        if self.matriz[atual_line][atual_col] == 'o':
            if not(new_line == atual_line - 1):
                print('!!! WRONG MOVE !!!')
                return False

            if self.matriz[new_line][new_col] == ' ':
                if atual_col + 1 == new_col or atual_col - 1 == new_col:
                    self.matriz[new_line][new_col] = 'o'
                    self.matriz[atual_line][atual_col] = ' '
                    if new_line == 1:
                        print(
                            '\t\t --> Congratulations {}, now you have a King'
                            .format(str(self.player)))
                        self.matriz[new_line][new_col] = 'O'
                    return True

            elif self.matriz[new_line][new_col].lower() == 'x':
                unidade = -1 if new_col < atual_col else 1

                if self.matriz[new_line + unidade][new_col + unidade] == ' ':
                    self.matriz[new_line][new_col] = ' '
                    self.matriz[new_line + unidade][new_col + unidade] = 'o'
                    self.count_point()
                    if new_line == 1:
                        print(
                            '\t\t --> Congratulations {}, now you have a King'
                            .format(str(self.player)))
                        self.matriz[new_line][new_col] = 'O'
                    return True
            print('!!! WRONG MOVE !!!')
            return False

        elif self.matriz[atual_line][atual_col] == 'x':
            if not(new_line == atual_line + 1):
                print('!!! WRONG MOVE !!!')
                return False

            if self.matriz[new_line][new_col] == ' ':
                if atual_col + 1 == new_col or atual_col - 1 == new_col:
                    self.matriz[new_line][new_col] = 'x'
                    self.matriz[atual_line][atual_col] = ' '
                    if new_line == 8:
                        print('Congratulations player 2, now you have a King')
                        self.matriz[new_line][new_col] = 'X'
                    return True
            elif self.matriz[new_line][new_col].lower() == 'o':
                unidade = -1 if new_col < atual_col else 1

                if self.matriz[new_line + unidade][new_col + unidade] == ' ':
                    self.matriz[new_line][new_col] = ' '
                    self.matriz[atual_line][atual_col] = ' '
                    self.matriz[new_line + unidade][new_col + unidade] = 'x'
                    self.count_point()
                    if new_line == 1:
                        print('Congratulations player 2, now you have a King')
                        self.matriz[new_line][new_col] = 'X'
                    return True
            print('!!! WRONG MOVE !!!')
            return False

        elif self.matriz[atual_line][atual_col] == 'O':
            return self.king_walk('O', casa_atual, casa_nova)

        elif self.matriz[atual_line][atual_col] == 'X':
            return self.king_walk('X', casa_atual, casa_nova)

    def king_walk(self, item, casa_atual, casa_nova):
        atual_line, atual_col = self.detach_item(casa_atual)
        new_line, new_col = self.detach_item(casa_nova)

        total_lines = atual_line - new_line
        total_cols = atual_col - new_col
        step_lines = -1 if total_lines > 0 else 1
        step_cols = -1 if total_cols > 0 else 1
        aux_col, aux_line = atual_col, atual_line
        if abs(total_lines) != abs(total_cols):
            print('!!! WRONG MOVE !!!')
            return False

        for _ in range(abs(total_lines)):
            aux_col += step_cols
            aux_line += step_lines
            if self.matriz[aux_line][aux_col] == ' ':
                continue
            if self.matriz[aux_line][aux_col].lower() != item.lower():
                self.matriz[aux_line][aux_col] = ' '
                new_line = new_line + step_lines
                new_col = new_col + step_cols
                self.count_point()
                continue
            break

        else:
            self.matriz[new_line][new_col] = item
            self.matriz[atual_line][atual_col] = ' '
            return True

        print('!!! WRONG MOVE !!!')
        return False

    def count_point(self):
        self.score[self.player.char] += 1
        self.player.points += +1
        print('~> Congratulations, {}! You get it.'.format(str(self.player)))

    def verify_game_over(self):
        items = 0
        for line, _ in enumerate(self.matriz):
            for column, _ in enumerate(self.matriz[line]):
                if self.matriz[line][column] in ('x', 'X') or \
                        self.matriz[line][column] in ('o', 'O'):
                    items += 1

        if items <= 3:
            print('\t\t ~~~~~ GAME OVER ~~~~~')

            self.game_over()

    def game_over(self):
        x = self.score['x']
        o = self.score['o']

        print('\n\t***\n\t\tPontuação: Jogador 1: {}, Jogador 2: {}'.format(
            o, x))

        if o > x:
            print('Jogador 1 venceu com {} pontos!'.format(x))
        else:
            print('Jogador 2 venceu com {} pontos!'.format(o))

        exit()

    def round(self):
        self.define_player()
        line = None
        column = None

        verify_player = False
        while verify_player is False:
            initial_piece = input('Qual peça você gostaria de movimentar? ')
            line, column = self.detach_item(initial_piece)
            peca = self.matriz[line][column]
            validate_player = self.validate_player(peca)
            if validate_player is False:
                continue
            print('Para onde você gostaria de mover sua peça?')
            # self.hint_move(line, column)
            atual_piece = input('Digite no console sua resposta: ')
            if self.verify_move(initial_piece, atual_piece) is True:
                break

        self.count_shift()
        self.verify_game_over()
        self.start()

    def hint_move(self, line, column):
        piece = self.matriz[line][column]

        for key, val in self.board.letters.items():
            if piece == 'o':
                if val == line - 1:
                    option = key
                    if not column + 1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            option, column + 1))
                    if not column - 1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            option, column - 1))
            if piece == 'x':
                if val == line + 1:
                    option = key
                    if not column + 1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            option, column + 1))
                    if not column - 1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            option, column - 1))

            if piece in ('O', 'X'):
                break

    def validate_player(self, peca):
        if self.player.char == peca.lower():
            return True

        else:
            print(
                '!!! Desculpe, mas esse movimento é impropio. Sua peça é a '
                '"{}" e você está tentando mover é a {}.'.format(
                    self.player.char, peca))
            return False

    def detach_item(self, coordenadas):
        try:
            return self.board.letters[coordenadas[0]], int(coordenadas[1])
        except KeyError:
            print('>>> Por favor, tente uma coordenada válida!')
            return ('q', 'q')

    def count_shift(self):
        self.shift += 1


if __name__ == "__main__":
    game = Game()
    game.start()
