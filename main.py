from datetime import datetime, timedelta

import pygame

from canvas import Canvas
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    clock = pygame.time.Clock()
    end_time = None

    canvas = Canvas(WIN, pygame.Rect(10, 10, WIN.get_width() / 3, WIN.get_height() - 20))
    font = pygame.font.Font(None, 32)
    lbl = font.render(f"Time left: 60", True, BLACK)
    WIN.blit(lbl, (canvas.rect.width + 10, 10))

    while run:
        clock.tick(FPS)

        if end_time is not None:
            pygame.draw.rect(WIN, BG, pygame.Rect(canvas.rect.width + 10, 10, 450, 30))
            lbl = font.render(f"Time left: {int((end_time - datetime.now()).total_seconds())}", True, BLACK)
            WIN.blit(lbl, (canvas.rect.width + 10, 10))

        WIN.blit(pygame.image.load("imgs/pixel_art_img1.png"), (canvas.rect.width * 2 - 5, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and end_time is None:
                end_time = datetime.now() + timedelta(seconds=60)

            if pygame.mouse.get_pressed()[0]:
                canvas.draw_square(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[2]:
                canvas.remove_squere(pygame.mouse.get_pos())

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    pygame.display.set_caption(TITLE)

    WIN.fill(BG)
    pygame.display.update()

    pygame.init()
    main()
