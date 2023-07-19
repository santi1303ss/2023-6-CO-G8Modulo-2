import pygame

from game.utils.constants import (
    FONT_STYLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WALLPAPER,
    WALLPAPER2,
    ICON, FONT_BODY, FONT_TITLE
)


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, message_2, message_3,screen  ): # TITLE = "SPACE XD"):
        screen.fill((255, 255, 255))
        #ADD FONTS FOR GAME AND BODY OF GAME
        self.font = pygame.font.Font(FONT_BODY, 30)
        #self.font_title = pygame.font.Font(FONT_TITLE, 100)#Implemetar
        #self.font_result = pygame.font.Font(FONT_TITLE, 30)
        
        self.icon = pygame.transform.scale(ICON, (120, 80))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self. HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        self.text_2 = self.font.render(message_2, True, (0, 0, 0))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2 = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 200)
        self.text_3 = self.font.render(message_3, True, (0, 0, 0))
        self.text_rect_3 = self.text_3.get_rect()
        self.text_rect_3 = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 300)
        self.wallpaper = pygame.transform.scale(
            WALLPAPER, (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

    def update(self, game):
        pygame.display.update()
        self.manager_events_on_menu(game)

    def draw(self, screen, game):
        screen.blit(self.wallpaper, [0, 0])
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_2, self.text_rect_2)
        screen.blit(self.text_3, self.text_rect_3)

    def manager_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.run()

    def reset_screen_color(self, screen):
        screen.fill((0, 0, 0))
        

    def update_message(self, message, message_2, message_3):
        self.text = self.font.render(message, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect = (
            self.HALF_SCREEN_WIDTH - 200,
            self.HALF_SCREEN_HEIGHT - 80,
        )

        # texto 2
        self.text_2 = self.font.render(message_2, True, (255, 255, 255))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2 = (
            self.HALF_SCREEN_WIDTH - 200,
            self.HALF_SCREEN_HEIGHT + 25,
        )
        # texto 3
        self.text_3 = self.font.render(message_3, True, (255, 255, 255))
        self.text_rect_3 = self.text_3.get_rect()
        self.text_rect_3 = (
            self.HALF_SCREEN_WIDTH - 200,
            self.HALF_SCREEN_HEIGHT + 130,
        )
        self.wallpaper = pygame.transform.scale(
            WALLPAPER2, (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
