import pygame
from board import Board

pygame.init()


class Game():
    global board
    board = Board()
    display = pygame.display.set_mode([board.width, board.height])

    def create_display(self):
        """
            all info about create display
        """
        pygame.display.set_caption('Checkers')
        pygame.font.init()

        while (1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.avalia_clique(pygame.mouse.get_pos())

            board.draw_board(self.display)
            self.display.fill(board.black_color)

    def main_menu(self):
        pass
