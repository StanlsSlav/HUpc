import os
import random as rand
from datetime import datetime, timedelta

import pygame

import image_comparer
from canvas import Canvas
from constants import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def pick_random_image() -> str:
    images = os.listdir("imgs/")

    try:
        images.remove("screenshot.png")
    except ValueError:
        pass

    return f"imgs/{images[rand.randint(0, len(images) - 1)]}"


def start_game():
    WIN.fill(BG)

    run = True
    clock = pygame.time.Clock()
    end_time = None
    left_time = -1

    pygame.init()

    canvas = Canvas(WIN, pygame.Rect(10, 10, WIN.get_width() / 3, WIN.get_height() - 20))
    font = pygame.font.Font(None, 32)

    drawn_image = "imgs/screenshot.png"
    model_image = pick_random_image()

    while run:
        clock.tick(FPS)

        if end_time is not None:
            # Fix the overwrite on self
            pygame.draw.rect(WIN, BG, pygame.Rect(canvas.rect.width + 15, 0, canvas.rect.width, canvas.rect.height))

            left_time = max(int((end_time - datetime.now()).total_seconds()), 0)
            timer_lbl = font.render(f"Time left: {left_time}", True, BLACK)
            WIN.blit(timer_lbl, (canvas.rect.width + canvas.rect.width / 3 - 1, 50))

        WIN.blit(pygame.image.load(model_image), (WIN.get_width() / 3 * 2 - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and end_time is None:
                end_time = datetime.now() + timedelta(seconds=PLAY_TIME + 1)

            if pygame.mouse.get_pressed()[0]:
                canvas.draw_square(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[2]:
                canvas.remove_square(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                canvas.create_img()

        if left_time == 0:
            canvas.create_img()

            similarity_percent = int(100 - image_comparer.rms_diff(drawn_image, model_image))
            divider = 4

            # Clamp the percent within allowed boundaries
            if similarity_percent < 0:
                similarity_percent = 0
            elif similarity_percent > 100:
                similarity_percent = 100

            # What's the result of the game?
            if similarity_percent < 25:
                result = "Improvable"
            elif similarity_percent < 50:
                result = "Pretty good"
            elif similarity_percent < 75:
                result = "Almost there"
            elif similarity_percent < 100:
                result = "That's good! Real good"
                divider = 11
            else:
                result = "Is that you, Leonardo?!"
                divider = 13

            # Fix the overwrite on self
            pygame.draw.rect(WIN, BG, pygame.Rect(canvas.rect.width + 15, 0, canvas.rect.width, canvas.rect.height))

            similarity_lbl = font.render(f"{result} - {similarity_percent}%", True, BLACK)
            WIN.blit(similarity_lbl, (canvas.rect.width + canvas.rect.width / divider - 1, WIN.get_height() - 100))

            (end_time, left_time) = (None, -1)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    pygame.display.set_caption(TITLE)
    start_game()
