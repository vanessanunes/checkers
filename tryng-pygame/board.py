import pygame

class Board():
    def draw_board(self, board, color, size):
        """
            draw board
        """
        print('draw display')
        pygame.draw.rect(board, color, pygame.Rect(size))
        pygame.display.flip()
