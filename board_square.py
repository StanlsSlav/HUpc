import pygame
from pygame import Rect, Surface

from constants import ROWS, COLS


class BoardSquare:
    def __init__(self, win: Surface, color: tuple[int, int, int], canvas, mouse_pos: tuple[int, int]):
        (c_top, c_left, c_width, c_height) = canvas.rect
        (mouse_x, mouse_y) = mouse_pos
        offset = 1

        mouse_x -= c_left
        mouse_y -= c_top

        self.width: float = c_width / COLS
        self.height: float = c_height / ROWS
        self.color = color

        square = Rect(0, 0, self.width, self.height)

        for row in range(ROWS):
            start_y = int(row * self.height)
            end_y = int(row * self.height + self.height)

            if mouse_y not in range(start_y, end_y):
                continue

            if row == ROWS - 1:
                square.top = float(row * self.height + c_top - offset)
            else:
                square.top = float(row * self.height + c_top + offset)
            break

        for col in range(COLS):
            start_x = int(col * self.width)
            end_x = int(col * self.width + self.width)

            if mouse_x not in range(start_x, end_x):
                continue

            if col == COLS - 1:
                square.left = float(col * self.width + c_left - offset)
            else:
                square.left = float(col * self.width + c_left + offset)
            break

        pygame.draw.rect(win, self.color, square)
        pygame.display.update()
