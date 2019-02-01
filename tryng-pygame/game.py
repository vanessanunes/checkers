import pygame
from board import Board

pygame.init()

class Game():
    global board
    board = Board()
    # global display
    display = pygame.display.set_mode([board.heigth, board.width])
    

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

            board.draw_board(self.display)
            self.display.fill(board.black_color)
            # display.draw_board(display, board.white_color, [1, 5, 40, 50])



    def main_menu(self):
        pass
