from settings import *
from machine import Machine
import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot_Demo')
        self.clock = pygame.time.Clock()
        self.menu_bg = pygame.image.load(MENU_IMAGE_PATH)
        self.menu()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT-80))

        self.machine = Machine()
        self.delta_time = 0

        bg_music = pygame.mixer.Sound('SLOTS PY/Vantage_5050.mp3')
        bg_music.play(loops=-1)

    def menu(self):
        self.menu_bg = pygame.transform.scale(self.menu_bg, (WIDTH, HEIGHT))
        self.screen.blit(self.menu_bg, (0,0))
        MENU_FONT = pygame.font.SysFont('Corbel', 100)  
        MENU_FONT_COLOR = (255,255,255)
        MENU_TEXT = MENU_FONT.render('PLAY' , True , MENU_FONT_COLOR)
        self.screen.blit(MENU_TEXT, (self.screen.get_width()/2 - 100, self.screen.get_height()/2))
        x = True
        while(x):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = False     
            pygame.display.update()


    def run(self):

        self.start_time = pygame.time.get_ticks()

        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0,0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

