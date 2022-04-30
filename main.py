from datetime import datetime, timedelta

import pygame

import image_comparer
from canvas import Canvas
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    clock = pygame.time.Clock()
    end_time = None
    left_time = 0

    canvas = Canvas(WIN, pygame.Rect(10, 10, WIN.get_width() / 3, WIN.get_height() - 20))
    font = pygame.font.Font(None, 32)
    lbl = font.render(f"Time left: 60", True, BLACK)
    WIN.blit(lbl, (canvas.rect.width + 10, 10))

    drawn_image = "imgs/screenshot.png"
    model_image = "imgs/pixel_art_img2.png"

    while run:
        clock.tick(FPS)

        if end_time is not None:
            # Fix the overwrite on self
            pygame.draw.rect(WIN, BG, pygame.Rect(canvas.rect.width + 10, 10, 450, 30))

            left_time = max(int((end_time - datetime.now()).total_seconds()), 0)
            lbl = font.render(f"Time left: {left_time}", True, BLACK)
            WIN.blit(lbl, (canvas.rect.width + 10, 10))

        WIN.blit(pygame.image.load(model_image), (WIN.get_width() / 3 * 2 - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and end_time is None:
                end_time = datetime.now() + timedelta(seconds=PLAY_TIME)

            if pygame.mouse.get_pressed()[0]:
                canvas.draw_square(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[2]:
                canvas.remove_square(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                canvas.create_img()

        if left_time == 0:
            canvas.create_img()

            # Redraw canvas to as new and then show on screen the results
            print(f"Similarity {image_comparer.rmsdiff(drawn_image, model_image)}")
            (end_time, left_time) = (None, -1)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    pygame.display.set_caption(TITLE)

    WIN.fill(BG)
    pygame.display.update()

    pygame.init()
    main()
