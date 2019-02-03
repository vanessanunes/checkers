# -*- coding: utf-8 -*-
class Game():

    matriz_players = [
        ['/', '1', '2', '3', '4', '5', '6', '7', '8'],
        ['a', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        ['b', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['c', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        ['d', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['f', ' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['g', 'o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        ['h', ' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o']
    ]
    letras = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }
    players = ('x', 'o')
    player = None
    score = {
    'x': 0,
    'o': 0,
    }
    shift = 1

    def start(self):
        print('\t ** Welcome to the Checkers Game! ** ')
        self.show_matriz()
        self.jogada()

    def show_matriz(self):
        for i in self.matriz_players:
            print('\t {}'.format(i))

    def verifica_movimentacao(self, casa_atual, casa_nova):
        print('jogador: {}'.format(self.player))

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)
        
        if casa_linha_nova == casa_linha_atual:
            print('Não pode mover para a mesma linha, mova para a próxima linha')
            return False

        if casa_col_nova == casa_col_atual:
            print('Não pode mover para a mesma coluna, mova para a próxima coluna')
            return False

        if self.player is 'o':
            if casa_linha_nova > casa_linha_atual:
                print('Não pode mover para trás!')
                return False
            # pontuação, caso a casa nova tiver peça adversario, pontuar
            if self.matriz_players[casa_linha_nova][casa_col_nova] is 'x':
                self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                self.count_point()
             
        if self.player is 'x':
            if casa_linha_atual > casa_linha_nova:
                print('Não pode mover para trás!')
                return False
            if self.matriz_players[casa_linha_nova][casa_col_nova] is 'o':
                self.matriz_players[casa_linha_nova][casa_col_nova] = ' '
                self.count_point()

        return True

    def count_point(self):
        self.score[self.player] += 1
        print('~> Parabéns ao jogador {}! Fez mas um ponto. \n\tPontuação total de {}'.format(self.player, self.score[self.player]))

    def atualizar_matriz(self, casa_atual, casa_nova):
        print('atualizar_matriz: atual: {}, nova: {}'.format(casa_atual, casa_nova))
        if not self.verifica_movimentacao(casa_atual, casa_nova):
            print('Tente escolher a pŕoxima jogada')
            return False

        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)

        peca_atual = self.matriz_players[casa_linha_atual][casa_col_atual]
        peca_nova = self.matriz_players[casa_linha_nova][casa_col_nova]

        self.matriz_players[casa_linha_atual][casa_col_atual] = peca_nova
        self.matriz_players[casa_linha_nova][casa_col_nova] = peca_atual

        return True

    def jogada(self):
        shift = self.shift % 2
        self.player = self.players[shift]
        print('~> Vez do jogador {}, shift {}'.format(self.player, shift))

        linha = None
        coluna = None

        valida_peca_jogador = False
        while valida_peca_jogador is False:
            peca_inicial = input('Qual peça você gostaria de movimentar? ')
            linha, coluna = self.desmonta_peca(peca_inicial)
            peca = self.matriz_players[linha][coluna]
            validar_peca_jogador = self.validar_peca_jogador(peca)
            if validar_peca_jogador is True:
                break

        move_peca = False
        while move_peca == False:
            print('Para onde você gostaria de mover sua peça?\n')
            self.sugestao_movimento(linha, coluna)
            peca_atual = input('Digite no console sua resposta: ')
            if self.atualizar_matriz(peca_inicial, peca_atual) is True:
                move_peca = True
            
        self.count_shift()
        self.start()


    def sugestao_movimento(self, linha, coluna):
        for key, val in self.letras.items():
            if self.player is 'o':
                if val == linha-1:
                    opcao_letra = key
                    if not coluna+1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna+1))
                    if not coluna-1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna-1))
            if self.player is 'x':
                if val == linha+1:
                    opcao_letra = key
                    if not coluna+1 >= 9:
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna+1))
                    if not coluna-1 <= 0:
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna-1))

    def validar_peca_jogador(self, peca):
        # import pdb
        # pdb.set_trace()
        if self.player is peca:
            print('Ok, vc é o jogador certo')
            return True

        else:
            print(
                '!!! Desculpe, mas esse movimento é impropio. Sua peça é a "{}" ' \
                'e você está tentando mover é a {}.'.format(self.player, peca))
            return False


    def desmonta_peca(self, coordenadas):
        
        while True:
            try:
                return self.letras[coordenadas[0]], int(coordenadas[1])
                False
            except KeyError:
                print('Por favor, tente uma coordenada válida!')
                return ('q', 'q')

    def count_shift(self):
        self.shift += 1

if __name__ == "__main__":
    game = Game()
    game.start()
