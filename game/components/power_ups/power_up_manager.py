import random

import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart

from game.utils.constants import HEART, SPACESHIP, SPACESHIP_SHIELD


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        pass