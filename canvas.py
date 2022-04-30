﻿import pygame
from pygame import Rect

from board_square import BoardSquare
from constants import BLACK, WHITE


class Canvas:
    def __init__(self, win, rect: Rect):
        self.win = win
        self.rect: Rect = rect

        pygame.draw.rect(self.win, BLACK, self.rect, 1, 1)
        pygame.display.flip()

    def draw_square(self, mouse_pos: (int, int)):
        (mouse_x, mouse_y) = mouse_pos

        if mouse_x not in range(self.rect.left, self.rect.left + self.rect.width) or \
                mouse_y not in range(self.rect.top, self.rect.top + self.rect.height):
            return

        BoardSquare(self.win, BLACK, self, mouse_pos)

    def remove_squere(self, mouse_pos: (int, int)):
        (mouse_x, mouse_y) = mouse_pos

        if mouse_x not in range(self.rect.left, self.rect.left + self.rect.width) or \
                mouse_y not in range(self.rect.top, self.rect.top + self.rect.height):
            return

        BoardSquare(self.win, WHITE, self, mouse_pos)

    def create_img(self):
        sub = self.win.subsurface(self.rect)
        pygame.image.save(sub, "screenshot.jpg")
