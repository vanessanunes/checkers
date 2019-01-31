import pygame
from board import Board

pygame.init()

heigth = 800
width = 600
display = pygame.display.set_mode([heigth, width])

black_color = (0, 0, 0)
white_color = (255, 255, 255)
board_color = (0, 31, 0)


class Game():

    def create_display(self):
        """
            all info about create display
        """
        pygame.display.set_caption('Checkers')
        pygame.font.init()

        while (1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            display.fill(black_color)
            board = Board()
            board.draw_board(display, white_color, [1, 5, 40, 50])