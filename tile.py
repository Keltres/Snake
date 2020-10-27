"""Tile class"""
import pygame

class Tile(pygame.Rect):

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (127, 255, 0)
    RED = (255, 0, 0)

    def __init__(self, screen, position, size):
        self.width, self.height = size, size
        self.top, self.left = position[0], position[1]
        self.screen = screen
        pygame.draw.rect(screen, Tile.WHITE, self)

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
