from settings import *
from machine import Machine
import pygame, sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Fruit Hunt Slot Machine')
        self.clock = pygame.time.Clock()
        self.menu_bg = pygame.image.load(MENU_IMAGE_PATH)

        bg_music = pygame.mixer.Sound('aesthetics/bg_music.mp3')
        bg_music.play(loops=-1)
        self.menu()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT-80))

        self.machine = Machine()
        self.delta_time = 0


    def menu(self):
        self.menu_bg = pygame.transform.scale(self.menu_bg, (WIDTH, HEIGHT))
        self.screen.blit(self.menu_bg, (0,0))
        MENU_FONT = pygame.font.Font(UI_FONT, 30)
        MENU_FONT_COLOR = (255,255,255)
        MENU_TEXT = MENU_FONT.render('CLICK  \'SPACE\'  TO PLAY' , True , MENU_FONT_COLOR)
        self.screen.blit(MENU_TEXT, (self.screen.get_width()/2 - 580, self.screen.get_height()/2))

        MENU_FONT_2 = pygame.font.Font(UI_FONT, 70)
        MENU_TEXT_2 = MENU_FONT_2.render('FRUIT HUNT!' , True , MENU_FONT_COLOR)
        self.screen.blit(MENU_TEXT_2, (self.screen.get_width()/2 - 600, self.screen.get_height()/2 - 210))
        x = True
        while(x):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
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

