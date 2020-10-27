"""The gird class"""
from random import randint

from tile import Tile
from constants import OFFSET, NUMBER_OF_BLOCKS, BLOCK_SIZE

class Grid():

    def __init__(self, size, NoB, screen):
        self.array = [[Tile(screen, (x*(size)+(OFFSET//2), y*(size)+(OFFSET//2)), size-OFFSET) for x in range(NoB)] for y in range(NoB)]
