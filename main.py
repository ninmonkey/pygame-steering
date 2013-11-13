__author__ = 'jake'

import os
import sys
from pygame import Color, Rect
import pygame as pg

class Game():
    """Game Controller"""
    def __init__(self):
        pg.init()
        pg.display.set_caption("Pygame-steering demo")
        self.screen = pg.display.set_mode((1024, 768))
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.
        self.done = False
        self.keys = pg.key.get_pressed()

        # boids

    def event_loop(self):
        # main event handling

        self.keys = pg.key.get_pressed() # Perhaps best inside? depends on time iterating
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True

    def main_loop(self):
        """ events, physics, render"""
        while not self.done:
            self.event_loop()
            self.screen.fill(Color("gray50"))

            # self.player.update(self.screen, self.keys)

            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.main_loop()
    pg.quit()
    sys.exit()

    print("done")
