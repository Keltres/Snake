"""berry class"""

import pygame
from random import choice

from constants import BLOCK_SIZE, OFFSET, NUMBER_OF_BLOCKS
from tile import Tile

class Berry(Tile):

    def __init__(self, screen, size, snake):
        
        self.picked = False

        all_indexes = [[j, i] for i in range(NUMBER_OF_BLOCKS) for j in range(NUMBER_OF_BLOCKS)]
        
        snake_indexes = snake.get_snake_indexes()
        
        for index_pair in snake_indexes:
            all_indexes.remove(index_pair)

        [x, y] = choice(all_indexes)
        
        Tile.__init__(self, screen, (x*size+(OFFSET//2), y*size+(OFFSET//2)), BLOCK_SIZE-OFFSET)
        pygame.draw.rect(screen, Tile.RED, self)
