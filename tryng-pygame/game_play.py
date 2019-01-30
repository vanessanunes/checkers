import pygame

# ref https://github.com/LukeHxH/mp_damas/blob/master/iniciar_jogo.py

pygame.init()

heigth = 800
width = 600

black_pieces = (0, 0, 0)
white_pieces = (255, 255, 255)

board = pygame.display.set_mode(heigth, width)
pygame.display.set_caption('Checkers')
pygame.font.init()


class Game():

    def __init__(self):
        self.gamers = ('x', 'o')
        self.board = [
            ['x','-','x','-','x','-','x','-']
            ['-','x','-','x','-','x','-','x'],
            ['x','-','x','-','x','-','x','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','o','-','o','-','o','-','o'],
            ['o','-','o','-','o','-','o','-'],
            ['-','o','-','o','-','o','-','o']
        ]

