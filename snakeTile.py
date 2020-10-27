"""class for snake's body
    adds the connectivity functionality
"""
import pygame
from tile import Tile

class SnakeTile(Tile):

    def __init__(self, screen, position, size):
        Tile.__init__(self, screen, position, size)
        pygame.draw.rect(screen, Tile.GREEN, self)
        self.direction = [0, 0]