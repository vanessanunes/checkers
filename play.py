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
            self.player.name, self.player.char.piece, self.shift + 1))

    def verifica_movimentacao(self, casa_atual, casa_nova):
        # print('verifica_movimentacao')
        linha_atual, col_atual = self.desmonta_peca(casa_atual)
        linha_nova, col_nova = self.desmonta_peca(casa_nova)

        if linha_nova == linha_atual or col_atual == col_nova:
            print('movimento inválido, tente novamente')
            return False


        if self.matriz_players[linha_atual][col_atual] == 'o':
            # se a linha for diferente, ou seja subindo OK
            if not(linha_nova == linha_atual - 1):
                print('movimento inválido')
                return False

            if self.matriz_players[linha_nova][col_nova] == ' ':
                if col_atual + 1 == col_nova or col_atual - 1 == col_nova:
                    self.matriz_players[linha_nova][col_nova] = 'o'
                    self.matriz_players[linha_atual][col_atual] = ' '
                    if linha_nova == 1:
                        print('Congratulations player 2, now you have a King')
                        self.matriz_players[linha_nova][col_nova] = 'O'
                    return True

            elif self.matriz_players[linha_nova][col_nova].lower() == 'x':
                unidade = -2 if col_nova < col_atual else 2
                if self.matriz_players[linha_nova + unidade][col_nova + unidade] == ' ':
                    self.matriz_players[linha_nova][col_nova] = ' '
                    self.matriz_players[linha_nova + unidade][col_nova + unidade] = 'o'
                    self.count_point()
                    if linha_nova == 1:
                        print('Congratulations player 2, now you have a King')
                        self.matriz_players[linha_nova][col_nova] = 'O'
                    return True
            print('movimento inválido')
            return False
        
        if self.matriz_players[linha_atual][col_atual] == 'x':
            if not(linha_nova == linha_atual + 1):
                print('movimento inválido')
                return False

            if self.matriz_players[linha_nova][col_nova] == ' ':
                if col_atual + 1 == col_nova or col_atual - 1 == col_nova:
                    self.matriz_players[linha_nova][col_nova] = 'x'
                    self.matriz_players[linha_atual][col_atual] = ' '
                    if linha_nova == 8:
                        print('Congratulations player 2, now you have a King')
                        self.matriz_players[linha_nova][col_nova] = 'X'
                    return True
            elif self.matriz_players[linha_nova][col_nova].lower() == 'o':
                unidade = -2 if col_nova < col_atual else 2
                if self.matriz_players[linha_nova + unidade][col_nova + unidade] == ' ':
                    self.matriz_players[linha_nova][col_nova] = ' '
                    self.matriz_players[linha_nova + unidade][col_nova + unidade] = 'x'
                    self.count_point()
                    if linha_nova == 1:
                        print('Congratulations player 2, now you have a King')
                        self.matriz_players[linha_nova][col_nova] = 'X'
                    return True
            print('movimento inválido')
            return False

        if self.matriz_players[linha_atual][col_atual] == 'O':
            # if linha_atual == col_atual:
            #     print('movimento inválido col')
            #     return False

            # ela pula mais de uma casa
            step_l = -1 if linha_atual > linha_nova else 1
            step_c = -1 if col_atual > linha_nova else 1


            passos = linha_atual - col_atual
            unidade = -passos if passos < 0 else passos

            for i in range(1, unidade+1):
                import ipdb
                ipdb.set_trace()
                if col_atual+1
                # negativo ou positivo?? HEEELP


            # for i in range(passos)

            linha_aux = 0
            col_aux = 0
            # verifica se movimentacao é valida
            for linha in range(linha_atual, col_atual, step_l):
                for col in range(linha_nova, col_nova, step_c):
                    import ipdb
                    ipdb.set_trace()
                    if linha == linha_atual and col == col_atual:
                        continue
                    if self.matriz_players[linha][col] == ' ':
                        print('sem coisas no caminho')
                        continue
                    if self.matriz_players[linha][col].lower() == 'o':
                        print(self.matriz_players[linha][col].lower())
                        print('movimentacao invalida, tem coisa no caminho')
                        return False



            import ipdb
            ipdb.set_trace()






        # caso mover peça dama
        if self.matriz_players[casa_linha_atual][casa_col_atual] == 'O':
            print('Dama 0')
            if (casa_col_atual - casa_col_nova) < 0:
                casa_check = casa_col_nova + 1
            else:
                casa_check = casa_col_nova - 1

            if not self.matriz_players[casa_linha_nova - 1][casa_check] == ' ':
                print('Movimento inválido pois não espaço vázio para movimento')
                return False

            step_l = -1 if casa_linha_atual > casa_linha_nova else 1
            step_c = -1 if casa_col_atual > casa_linha_nova else 1

            for linha in range(casa_linha_atual, casa_linha_nova, step_l):
                for cl in range(casa_col_atual, casa_linha_nova, step_c):
                    char_casa = self.matriz_players[linha][cl]
                    print('char que estamos passando pela casa: {} ({}{})'.format(
                        self.matriz_players[linha][cl], linha, cl))
                    self.matriz_players[linha][cl] == 'O'
                    if char_casa in ('o', 'O'):
                        print('Opa, chegamos no nosso limite..')
                        self.matriz_players[casa_linha_atual][
                            casa_col_atual] = ' '

            self.matriz_players[casa_linha_nova][casa_col_nova] = '0'
            self.matriz_players[casa_linha_atual][casa_col_atual] = ' '
            # self.count_point()

    def count_point(self):
        self.score[self.player.char.piece] += 1
        self.player.points += +1
        print(
            '~> Parabéns ao jogador {}! Fez mas um ponto. \n\tPontuação '
            'total de {}'.format(self.player.name, self.score[self.player.char.piece]))

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

        # self.verifica_final_jogo()

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
            # self.board.show_matriz()

        self.count_shift()
        self.start()

    def sugestao_movimento(self, linha, coluna):
        print('sugestao_movimento: {}, {}'.format(linha, coluna))
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

            if peca_da_vez in ('O', 'X'):
                # print('DAMA! Bora mexer a Dama!')
                break

            # if peca_da_vez == 'X':
            #     print('DAMA! Bora mexer a Dama!')
            #     break

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
