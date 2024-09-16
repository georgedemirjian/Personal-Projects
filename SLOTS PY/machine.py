import pygame
from settings import *
from reel import *

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_list = {}
        self.reel_index = 0

        self.set_reels()

    def update(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()

    def set_reels(self):
        if not self.reel_list:
            x_tl = 10
            y_tl = -220
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_tl = x_tl + 220 + X_OFFSET
                y_tl = y_tl 
            self.reel_list[self.reel_index] = Reel((x_tl, y_tl))
            self.reel_index += 1

