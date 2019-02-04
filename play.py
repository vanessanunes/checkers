# -*- coding: utf-8 -*-
from game.piece import Piece
from game.player import Player
from game.board import Board


class Game():
    board = Board()
    matriz_players = board.board
    

    players = [None, None]
    player = None
    score = {
        'x': 0,
        'o': 0,
    }
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
            self.player.name, self.player.char.piece, self.shift+1))

    def verifica_movimentacao(self, casa_atual, casa_nova):
        print('jogador: {}'.format(self.player.name))

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)
        if casa_linha_nova == casa_linha_atual:
            print(
                'Não pode mover para a mesma linha, mova para a próxima linha')
            return False

        if casa_col_nova == casa_col_atual:
            print(
                'Não pode mover para a mesma coluna, mova para a próxima '
                'coluna')
            return False

        if self.player == 'o':
            if casa_linha_nova > casa_linha_atual:
                print('Não pode mover para trás!')
                return False
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'x', 'X'):
                self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                self.count_point()
            if casa_linha_nova == 1:
                print('Congratulations player 1, now you have a King')
                self.matriz_players[casa_linha_nova][casa_col_nova] = 'O'
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'o', 'O'):
                print('Não pode comer a sua própria peça')

        if self.player == 'x':
            if casa_linha_atual > casa_linha_nova:
                print('Não pode mover para trás!')
                return False
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'o', 'O'):
                self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                self.count_point()
            if casa_linha_nova == 8:
                print('Congratulations player 2, now you have a King')
                self.matriz_players[casa_linha_nova][casa_col_nova] = 'X'
            if self.matriz_players[casa_linha_nova][casa_col_nova] in (
                    'x', 'X'):
                print('Não pode comer a sua própria peça')

        return True

    def count_point(self):
        self.score[self.player] += 1
        print(
            '~> Parabéns ao jogador {}! Fez mas um ponto. \n\tPontuação '
            'total de {}'.format(self.player, self.score[self.player]))

    def atualizar_matriz(self, casa_atual, casa_nova):
        print('atualizar_matriz: atual: {}, nova: {}'.format(
            casa_atual, casa_nova))
        if not self.verifica_movimentacao(casa_atual, casa_nova):
            print('Tente escolher a pŕoxima jogada')
            return False

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)

        peca_atual = self.matriz_players[casa_linha_atual][casa_col_atual]
        peca_nova = self.matriz_players[casa_linha_nova][casa_col_nova]

        self.matriz_players[casa_linha_atual][casa_col_atual] = peca_nova
        self.matriz_players[casa_linha_nova][casa_col_nova] = peca_atual

        self.verifica_final_jogo()

        return True

    def verifica_final_jogo(self):
        pecas = 0
        for linha in self.matriz_players:
            for coluna in self.matriz_players:
                import pdb
                pdb.set_trace()
                if self.matriz_players[linha][coluna] in ('x', 'X') or \
                        self.matriz_players[linha][coluna] in ('o', 'O'):
                    pecas += 1

        print(pecas)
        if pecas <= 3:
            print('Jogo acabou!')

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

    def jogada(self):
        self.define_player()
        linha = None
        coluna = None

        valida_peca_jogador = False
        while valida_peca_jogador is False:
            peca_inicial = input('Qual peça você gostaria de movimentar? ')
            linha, coluna = self.desmonta_peca(peca_inicial)
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
        print('sugestao_movimento: {}, {}'.format(linha, coluna))
        peca_da_vez = self.matriz_players[linha][coluna]

        for key, val in self.board.letters.items():
            if peca_da_vez == 'o':
                if val == linha-1:
                    opcao_letra = key
                    if not coluna+1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna+1))
                    if not coluna-1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna-1))
            if peca_da_vez == 'x':
                if val == linha+1:
                    opcao_letra = key
                    if not coluna+1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna+1))
                    if not coluna-1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(
                            opcao_letra, coluna-1))

            if peca_da_vez == 'O':
                print('DAMA! Bora mexer a Dama!')
                break

            if peca_da_vez == 'X':
                print('DAMA! Bora mexer a Dama!')
                break

    def validar_peca_jogador(self, peca):
        if self.player.char.piece == peca.lower():
            print('Ok, vc é o jogador certo')
            return True

        else:
            print(
                '!!! Desculpe, mas esse movimento é impropio. Sua peça é a '
                '"{}" e você está tentando mover é a {}.'.format(
                    self.player, peca))
            return False

    def desmonta_peca(self, coordenadas):
        while True:
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
