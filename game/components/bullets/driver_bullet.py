import pygame

class driverBullet():
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = [] 
            
    def update (self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)    
            
    def draw (self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.holder == 'enemy':
            self.enemy_bullets.append(bullet)
            
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []