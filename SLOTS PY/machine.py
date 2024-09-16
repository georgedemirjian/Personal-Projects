import pygame
from settings import *
from reel import *

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_list = {}
        self.reel_index = 0
        self.can_toggle = True
        self.spinning = False

        self.set_reels()

    
    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_moving:
                self.can_toggle = False
                self.spinning = True
        if not self.can_toggle and [self.reel_list[reel].reel_is_moving for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
        #if keys[pygame.K_SPACE] and self.can_toggle and self.currentPlayer.balance >= self.currentPlayer.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            #self.currentPlayer.place_bet()
            #self.machine_balance += self.currentPlayer.bet_size
            #self.currentPlayer.last_payout = None

    def update(self, delta_time):
        self.get_input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
        
    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

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
    
    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)


