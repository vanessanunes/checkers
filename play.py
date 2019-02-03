# -*- coding: utf-8 -*-
class Jogo():

    """
    Jogador 1 = o (indice 1)
    jogador 2 = x (indice 0)
    """

    matriz_jogadores = [
        ['/', '1', '2', '3', '4', '5', '6', '7', '8'],
        ['a', 'x', '-', 'x', '-', 'x', '-', 'x', '-'],
        ['b', '-', 'x', '-', 'x', '-', 'x', '-', 'x'],
        ['c', 'x', '-', 'x', '-', 'x', '-', 'x', '-'],
        ['d', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['e', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['f', '-', 'o', '-', 'o', '-', 'o', '-', 'o'],
        ['g', 'o', '-', 'o', '-', 'o', '-', 'o', '-'],
        ['h', '-', 'o', '-', 'o', '-', 'o', '-', 'o']
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

    jogadores = ('x', 'o')
    pontuacao = (0, 0)
    turno = 1

    def iniciar(self):
        for i in self.matriz_jogadores:
            # import pdb
            # pdb.set_trace()
            print('\t {}'.format(i))

        self.jogada()

    def atualizar_matriz(self, casa_atual, casa_nova):
        casa_linha_atual, casa_col_atual = self.desmonta_peca(casa_atual)
        casa_linha_nova, casa_col_nova = self.desmonta_peca(casa_nova)

        peca_atual = self.matriz_jogadores[casa_linha_atual][casa_col_atual]
        peca_nova = self.matriz_jogadores[casa_linha_nova][casa_col_nova]

        self.matriz_jogadores[casa_linha_atual][casa_col_atual] = peca_nova
        self.matriz_jogadores[casa_linha_nova][casa_col_nova] = peca_atual

        self.iniciar()

    def jogada(self):
        # turno 1 = jogador 1
        # turno 0 = jogador 2
        # self.turno(jogador)
        turno = self.turno % 2
        jogador = self.jogadores[turno]
        print('Vez do jogador {}'.format(jogador))

        linha = None
        coluna = None

        valida_peca_jogador = False
        
        while valida_peca_jogador is False:
            peca_inicial = input('Qual peça você gostaria de movimentar? ')
            linha, coluna = self.desmonta_peca(peca_inicial)
            peca = self.matriz_jogadores[linha][coluna]
            validar_peca_jogador = self.validar_peca_jogador(peca, jogador)

            if validar_peca_jogador is True:
                break

        print('Para onde você gostaria de mover sua peça?\n')
        self.sugestao_movimentacao(jogador, linha, coluna)
        print('Sugestão de movimentação ok??')
        
        #e1 ou e3
        peca_atual = input('Digite no console sua resposta: ')

        # import p?ace()
        self.conta_turno()
        self.atualizar_matriz(peca_inicial, peca_atual)

    def sugestao_movimentacao(self, jogador, linha, coluna):
        # if jogador is 'o':
        for key, val in self.letras.items():
            if jogador is 'o':
                if val == linha-1:
                    opcao_letra = key
                    import pdb
                    pdb.set_trace()
                    
                    if self.matriz_jogadores[val][coluna-1] is 'x':
                        self.pontuacao[0] += 1
                        print('Jogador {} fez um ponto! Total de {}'.format(jogador, self.pontuacao[0]))
                    if self.matriz_jogadores[val][coluna+1] is 'x':
                        self.pontuacao[0] += 1
                        print('Jogador {} fez um ponto! Total de {}'.format(jogador, self.pontuacao[0]))
                    if self.matriz_jogadores[val][coluna-1] is '-':
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna-1))
                    if self.matriz_jogadores[val][coluna+1] is '-':
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna+1))
                    if val <= 0 or val >= 9:
                        print('O "val" já está fora do perimetro: {}'.format(val))
            if jogador is 'x':
                if val == linha+1:
                    opcao_letra = key
                    if self.matriz_jogadores[val][coluna-1] is 'o':
                        self.pontuacao[1] += 1
                        print('Jogador {} fez um ponto! Total de {}'.format(jogador, self.pontuacao[0]))
                    if self.matriz_jogadores[val][coluna+1] is 'o':
                        self.pontuacao[1] += 1
                        print('Jogador {} fez um ponto! Total de {}'.format(jogador, self.pontuacao[0]))
                    if self.matriz_jogadores[val][coluna-1] is '-':
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna-1))
                    if self.matriz_jogadores[val][coluna+1] is '-':
                        print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna+1))
                    if val <= 0 or val >= 9:
                        print('O "val" já está fora do perimetro: {}'.format(val))
            # if val == linha+1
        # else:
        #         for key, val in self.letras.items():
        #             if val == linha-1:
        #                 opcao_letra = key
        #                 print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna-1))
        #                 print('Você tem a opção de: \n\t => {}{}'.format(opcao_letra, coluna+1))



    def validar_peca_jogador(self, peca, jogador):
        # import pdb
        # pdb.set_trace()
        if jogador is peca:
            print('Ok, vc é o jogador certo')
            return True

        else:
            print(
                '!!! Desculpe, mas esse movimento é impropio. Sua peça é a "{}" ' \
                'e você está tentando mover é a {}.'.format(jogador, peca))
            return False


    def desmonta_peca(self, coordenadas):
        
        while True:
            try:
                return self.letras[coordenadas[0]], int(coordenadas[1])
                False
            except KeyError:
                print('Por favor, tente uma coordenada válida!')
                return ('q', 'q')
    # def turno(self, ultimo_jogador):

    #     """
    #         fazer verificacao se o jogador ainda tem jogadas ou não
    #         se não, pode passar para o novo jogador
    #     """
    #     pass
    def conta_turno(self):
        self.turno += 1

if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()
