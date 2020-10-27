"""Snake class"""
import pygame

from snakeTile import SnakeTile
from constants import *

class Snake():

    def __init__(self, screen, position, size):
        self.array = []
        # head of the snake is the last element of the array
        # tail of the snake is the first element of the array
        self.direction = [0, 0]
        self.push(SnakeTile(screen, position, size))
        
    def push(self, element):
        self.array.insert(0, element)

    def move(self):
        """moving algorithm"""
        pygame.draw.rect(self.array[0].screen, self.array[0].BLACK, self.array[0])

        self.array[0].left = self.array[-1].left + self.direction[0]*(self.array[0].height + OFFSET)
        self.array[0].top = self.array[-1].top - self.direction[1]*(self.array[0].width + OFFSET)

        if self.array[0].left < 0 or self.array[0].left > WIDTH or self.array[0].top < 0 or self.array[0].top > HEIGHT:
            raise IndexError()

        self.array.append(self.array.pop(0))

        pygame.draw.rect(self.array[-1].screen, self.array[-1].GREEN, self.array[-1])
        # print(self.array[-1].left, self.array[-1].top)

    def eat(self, berry):
        if self.array[-1].left == berry.left and self.array[-1].top == berry.top:
            return True
        return False

    def is_cannibal(self):
        for index in range(len(self.array)-1):
            if self.array[-1].left == self.array[index].left and self.array[-1].top == self.array[index].top:
                return True
        return False

    def change_direction(self, new_dir):
        if not (new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            self.direction = new_dir

    def get_snake_indexes(self):
        return [[(x.top + OFFSET//2)//BLOCK_SIZE, (x.left + OFFSET//2)//BLOCK_SIZE] for x in self.array]
