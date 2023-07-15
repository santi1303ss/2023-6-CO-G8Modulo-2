import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self):
        self.image = random.choice([ENEMY_1, ENEMY_2])
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.SHIP_WIDTH)
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy' 
        self.shootSpace = pygame.time.get_ticks() + 500
        self.shoot_num = 0
        

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.bulletSpace(game.driver_bullet)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0
            
    def bulletSpace (self, driver_bullet):
        time_current = pygame.time.get_ticks()
        round_time = round((self.shootSpace - pygame.time.get_ticks())/1000)
        if round_time <= 0:
            bullet = Bullet(self)
            driver_bullet.add_bullet(bullet)
            self.shoot_num += 1
            self.shootSpace = pygame.time.get_ticks()+1000