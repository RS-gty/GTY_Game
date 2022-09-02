# import time
import pygame
import sys


class Player(object):
    def __init__(self):
        self.position = [0, 0]
        self.speed = 1
        self.inventory = []


def submit():
    print(114514)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 450))
    pygame.display.set_caption('GTY-game')
    icon = pygame.image.load('/data/icon.ico')
    pygame.display.set_icon(icon)

    surface_image = pygame.image.load("/data/player.png")
    image_rect = surface_image.get_rect()
    image_rect.center = (100, 100)
    screen.blit(surface_image, image_rect)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()


if __name__ == '__main__':
    main()
