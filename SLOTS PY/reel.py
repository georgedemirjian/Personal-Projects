import pygame
import random
from settings import *

class Reel:
    def __init__(self, coords):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_reels = list(IMAGES.keys())
        random.shuffle(self.shuffled_reels)
        self.shuffled_reels = self.shuffled_reels[:5]

        self.reel_is_moving = False

        for index, item in enumerate(self.shuffled_reels):
            self.symbol_list.add(Symbol(IMAGES[item], coords, index))
            coords = list(coords)
            coords[1] += 215
            coords = tuple(coords)
        
    def animate(self, delta_time):
        if self.reel_is_moving:
            self.delay_time -= (delta_time * 1000)
            self.spin_time -= (delta_time *1000)
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True
            if self.delay_time <= 0:
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 100

                    if symbol.rect.top > 750:
                        if reel_is_stopping:
                            self.reel_is_moving = False
                        symbol_idx = symbol.index
                        symbol.kill()
                        self.symbol_list.add(Symbol(IMAGES[random.choice(self.shuffled_reels)], ((symbol.x_val), -190), symbol_idx))

    
    def start_spin(self, delay_time):
        self.delay_time = delay_time
        self.spin_time = 1000 + delay_time
        self.reel_is_moving = True

class Symbol(pygame.sprite.Sprite):
    def __init__(self, filePath, coords, index):
        super().__init__()

        self.symbol_name = filePath.split('/')[3].split('.')[0]
        self.coords = coords
        self.index = index

        self.image = pygame.image.load(filePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (220, 220))
        self.rect = self.image.get_rect(topleft = coords)
        self.x_val = self.rect.left
    
    def update(self):
        pass


    
