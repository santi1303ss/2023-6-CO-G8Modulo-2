import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SPACESHIP, SCREEN_HEIGHT, ENEMY_1
class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    LIMIT_Y = 300

    def __init__(self):
        super().__init__()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        self.display_limit()

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        self.display_limit()

    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        self.display_limit()

    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        self.display_limit()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#Tarea 1
    def display_limit(self):
        if self.rect.x < 0: #Limite izquierdo
            self.rect.x = SCREEN_WIDTH #Reaparece lado derecho
        if self.rect.x > SCREEN_WIDTH: #D
            self.rect.x = 0 #R.. Iz
            
        if self.rect.y < self.LIMIT_Y: #Limite de Y
            self.rect.y = self.LIMIT_Y #Mantiene la pocision
        if self.rect.y > SCREEN_HEIGHT - self.SHIP_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.SHIP_HEIGHT
            
