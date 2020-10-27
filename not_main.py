"""Snake"""
import sys

import pygame
from grid import Grid
from snake import Snake
from snakeTile import SnakeTile
from berry import Berry
from constants import *

def initialize():
    pass

def main():
    """The main fucntion of snake game"""

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0,0,0))

    # Grid(BLOCK_SIZE, NUMBER_OF_BLOCKS, screen)
    snake = Snake(screen, ((WIDTH)//2 - BLOCK_SIZE + OFFSET//2, (HEIGHT)//2 - BLOCK_SIZE + OFFSET//2), BLOCK_SIZE-OFFSET)
    berry = Berry(screen, BLOCK_SIZE, snake)
    tail = None
    events_q = []

    while True:

        clock.tick(2)

        # events handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                events_q.append(event)

        while len(events_q) > 2:
            events_q.pop()
        
        if len(events_q) > 0:
            keypress = events_q.pop(0)

            if keypress.key == pygame.K_UP:
                snake.change_direction([0, 1])

            elif keypress.key == pygame.K_DOWN:
                snake.change_direction([0, -1])

            elif keypress.key == pygame.K_LEFT:
                snake.change_direction([-1, 0])

            elif keypress.key == pygame.K_RIGHT:
                snake.change_direction([1, 0])
        #event handling finished

        # mechanics
        try:
            snake.move()
        except IndexError:
            print("you lost")
            # erase_borad()
            break

        berry.picked = snake.eat(berry)     # falg for generating new berry
        cannibal = snake.is_cannibal()      # falg for snake biting itself

        # new berry generation
        if berry.picked:
            snake.push(tail)
            berry = Berry(screen, BLOCK_SIZE, snake)
            
        # snake biting itself
        elif cannibal:
            print("you lost")
            # clear the screen or draw a sign onto the screen
            break

        # save the tail of the snake for the drawinging in the next frame
        tail = SnakeTile(snake.array[0].screen, (snake.array[0].top, snake.array[0].left), snake.array[0].width)

        pygame.display.flip()

if __name__ == '__main__':
    main()
