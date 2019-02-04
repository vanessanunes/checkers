# -*- coding: utf-8 -*-
from game.piece import Piece
from game.player import Player
from game.board import Board


class Game():
    board = Board()
    matriz_players = board.board

    players = [None, None]
    player = None
    total_score = 0
    shift = 0

    def start(self):
        print('\t ** Welcome to the Checkers Game! ** ')
        self.create_players()
        self.board.show_matriz()
        self.jogada()

    def create_players(self):
        self.players[0] = Player('Player 1', 'o')
        self.players[1] = Player('Player 2', 'x')

    def define_player(self):
        if self.shift % 2 == 0:
            self.player = self.players[0]
        else:
            self.player = self.players[1]
        print('~> Player {} move the piece {}, shift {}'.format(
            self.player.name, self.player.char.piece, self.shift + 1))

    def verifica_movimentacao(self, casa_atual, casa_nova):
        print('--> Play {}, it\'s your turn!'.format(self.player.name))

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)

        type_piece = self.matriz_players[casa_linha_atual][casa_col_atual]

        if casa_linha_nova == casa_linha_atual:
            print(
                'Não pode mover para a mesma linha, mova para a próxima linha')
            return False

        if casa_col_nova == casa_col_atual:
            print(
                'Não pode mover para a mesma coluna, mova para a próxima '
                'coluna')
            return False

        if not (casa_col_atual - 1 == casa_col_nova or
                casa_col_atual + 1 == casa_col_nova) and \
                not (casa_linha_atual - 1 == casa_linha_nova or
                     casa_linha_atual + 1 == casa_linha_nova) and \
                type_piece in ('x', 'o'):
            print('Peças comuns só podem movimentar uma casa')
            return False

        if self.player.char.piece == 'o':
            if casa_linha_nova > casa_linha_atual:
                print('\t!!! Sorry! You can\'t move back!')
                return False

            # caminho da dama, enquanto for andando e existir peças, vai
            # colhendo
            for l in range(casa_linha_atual, casa_linha_nova):
                for c in range(casa_col_atual, casa_col_nova):
                    if self.matriz_players[l][c] in ('x', 'X'):
                        import pdb
                        pdb.set_trace*()
                        self.matriz_players[l][c] = ' '
                        self.count_point()
                    if self.matriz_players[l][c] in ('o', 'o'):
                        self.matriz_players[l][c]
                        break
                # print('ATUALIZAR COM A NOVA ATUALIZACAO')
                # import pdb
                # pdb.set_trace()

                casa_linha_nova -= 1
                if casa_col_atual > casa_col_nova:
                    casa_col_nova -= 1
                else:
                    casa_col_nova += 1

                casa_nova = self.montar_coordenadar(
                    casa_linha_nova - 1, casa_col_nova)
                print('CASA NOVA = {}'.format(casa_nova))
                self.atualizar_matriz(casa_atual, casa_nova)

                # self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                # self.count_point()

            if casa_linha_nova == 1:
                print('Congratulations player 1, now you have a King')
                self.matriz_players[casa_linha_nova][casa_col_nova] = 'O'
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'o', 'O'):
                print(':( You can\t kill your won mens! :(')

        if self.player.char.piece == 'x':
            if casa_linha_atual > casa_linha_nova:
                print('\t!!! Sorry! You can\'t move back!')
                return False

            import pdb
            pdb.set_trace()

            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'o', 'O'):
                self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                self.count_point()
            if casa_linha_nova == 8:
                print('Congratulations player 2, now you have a King')
                self.matriz_players[casa_linha_nova][casa_col_nova] = 'X'
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'x', 'X'):
                print(':( You can\t kill your won mens! :(')

        return True

    def count_point(self):
        self.player.points += 1
        self.total_score += 1
        print(
            '\t\t~> Congratulation to the {}! You get 1 more point. \n\tTotal '
            'Score {}'.format(self.player.name, self.total_score))

    def atualizar_matriz(self, casa_atual, casa_nova):
        print(casa_atual, casa_nova)
        if not self.verifica_movimentacao(casa_atual, casa_nova):
            print('\t Try to choose other man')
            return False

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)

        peca_atual = self.matriz_players[casa_linha_atual][casa_col_atual]
        peca_nova = self.matriz_players[casa_linha_nova][casa_col_nova]

        self.matriz_players[casa_linha_atual][casa_col_atual] = peca_nova
        self.matriz_players[casa_linha_nova][casa_col_nova] = peca_atual

        # self.verifica_final_jogo()

        return True

    def verifica_final_jogo(self):
        pecas = 0
        for linha in self.matriz_players:
            for coluna in linha:
                if coluna in ('x', 'X') or coluna in ('o', 'O'):
                    pecas += 1

        print('{} jogadas'.format(pecas))
        # corrigir essa porra aqui
        if pecas >= 3:
            print('Jogo acabou!')

            self.game_over()

    def game_over(self):
        x = self.score['x']
        o = self.score['o']

        print('\n\t***\t\t\t\t\t\t***\n\t\tPontuação: Jogador 1: {}, Jogador 2: {}'.format(
            o, x))

        if o > x:
            print('Jogador 1 venceu com {} pontos!'.format(x))
        elif o == x:
            print('Jogo empatado!')
        else:
            print('Jogador 2 venceu com {} pontos!'.format(o))

        exit()

    def jogada(self):
        self.define_player()
        linha = None
        coluna = None

        valida_peca_jogador = False
        while valida_peca_jogador is False:
            peca_inicial = input('Qual peça você gostaria de movimentar? ')

            linha, coluna = self.desmonta_peca(peca_inicial)
            if (linha or coluna) == 'q':
                continue

            print(peca_inicial, linha, coluna)
            peca = self.matriz_players[linha][coluna]
            validar_peca_jogador = self.validar_peca_jogador(peca)
            if validar_peca_jogador is True:
                break

        move_peca = False
        while move_peca is False:
            print('Para onde você gostaria de mover sua peça?')
            self.sugestao_movimento(linha, coluna)
            peca_atual = input('Digite no console sua resposta: ')
            if self.atualizar_matriz(peca_inicial, peca_atual) is True:
                move_peca = True
        self.count_shift()
        self.start()

    def sugestao_movimento(self, linha, coluna):
        # print('sugestao_movimento: {}, {}'.format(linha, coluna))
        peca_da_vez = self.matriz_players[linha][coluna]

        for key, val in self.board.letters.items():
            if peca_da_vez == 'o':
                if val == linha - 1:
                    opcao_letra = key
                    if not coluna + 1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna + 1))
                    if not coluna - 1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna - 1))
            if peca_da_vez == 'x':
                if val == linha + 1:
                    opcao_letra = key
                    if not coluna + 1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna + 1))
                    if not coluna - 1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna - 1))

            if peca_da_vez == 'O':
                print('DAMA! Bora mexer a Dama!')
                break

            if peca_da_vez == 'X':
                print('DAMA! Bora mexer a Dama!')
                break

    def validar_peca_jogador(self, peca):
        if self.player.char.piece == peca.lower():
            return True

        else:
            print(
                '!!! Desculpe, mas esse movimento é impropio. Sua peça é a '
                '"{}" e você está tentando mover é a {}.'.format(
                    self.player.char.piece, peca))
            return False

    def montar_coordenadar(self, linha, coluna):
        for key, value in self.board.letters.items():
            if value == linha:
                return '{}{}'.format(key, coluna)

    def desmonta_peca(self, coordenadas):
        if coordenadas == '' or len(coordenadas) > 2:
            print('Por favor, tente uma coordenada válida!')
            return ('q', 'q')
        try:
            return self.board.letters[coordenadas[0]], int(coordenadas[1])
            False
        except KeyError:
            print('Por favor, tente uma coordenada válida!')
            return ('q', 'q')

    def count_shift(self):
        self.shift += 1


if __name__ == "__main__":
    game = Game()
    game.start()
