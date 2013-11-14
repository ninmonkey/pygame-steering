__author__ = 'jake'

import os
import sys
from pygame import Color, Rect
import pygame as pg

BASE_SPRITES = {}

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.image_original = BASE_SPRITES['ship']
        self.image = self.image_original
        self.rect = self.image.get_rect()
        self.angle = 0.

        self.rect.center = pg.display.get_surface().get_rect().center

    def rotate(self, angle):
        pass

    def update(self, screen, keys):
        pass

    def draw(self, screen):
        #update rect using vectors
        screen.blit(self.image, self.rect)


class Game():
    """Game Controller"""
    def __init__(self):
        global BASE_SPRITES

        pg.init()
        pg.display.set_caption("Pygame-steering demo")
        self.screen = pg.display.set_mode((1024, 768))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.
        self.done = False
        self.keys = pg.key.get_pressed()

        # images
        BASE_SPRITES['ship'] = pg.image.load(os.path.join("art", "boid.png")).convert_alpha()

        # boids
        self.player = Player()

        #self.objects = pg.sprite.Group()

    def draw(self):
        self.player.draw()

    def event_loop(self):
        # main event handling

        self.keys = pg.key.get_pressed() # Perhaps best inside? depends on time iterating
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE] or self.keys[pg.K_SPACE]:
                self.done = True

    def main_loop(self):
        """ events, physics, render"""
        while not self.done:
            self.event_loop()
            self.screen.fill(Color("gray20"))

            self.player.update(self.screen, self.keys)
            #self.objects.update()

            self.player.draw(self.screen)
            #self.objects.draw()

            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.main_loop()
    pg.quit()
    sys.exit()
