import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):                  #ancho | altura
    B_SIZE = pygame.transform.scale(BULLET, (10, 20))
    B_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (10, 20))
    BULLETS = {'enemy' : B_ENEMY_SIZE}
    B_SPEED = 20
    
    def __init__(self, spaceshift):
        self.image = self.BULLETS[spaceshift.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.holder = spaceshift.type
        
        
    def update(self, bullets):
        if self.holder == 'enemy':
            self.rect.y += self.B_SPEED
            
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)
            
    def draw (self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        