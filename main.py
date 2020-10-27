"""Snake"""
import sys

import pygame
from grid import Grid
from snake import Snake
from snakeTile import SnakeTile
from berry import Berry
from constants import *

def main():
    """The main fucntion of snake game"""

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0,0,0))

    Grid(BLOCK_SIZE, NUMBER_OF_BLOCKS, screen)
    snake = Snake(screen, ((WIDTH)//2 - BLOCK_SIZE + OFFSET//2, (HEIGHT)//2 - BLOCK_SIZE + OFFSET//2), BLOCK_SIZE-OFFSET)

    berry = Berry(screen, BLOCK_SIZE, snake)
    
    tail = SnakeTile(snake.array[-1].screen, (snake.array[-1].top, snake.array[-1].left), snake.array[-1].width)

    while True:

        clock.tick(2)

        # events handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction([0, 1])

                elif event.key == pygame.K_DOWN:
                    snake.change_direction([0, -1])

                elif event.key == pygame.K_LEFT:
                    snake.change_direction([-1, 0])

                elif event.key == pygame.K_RIGHT:
                    snake.change_direction([1, 0])

        snake.move()
        berry.picked = snake.eat(berry)
        cannibal = snake.is_cannibal()

        if berry.picked:
            snake.push(tail)
            # berry.picked = False
            berry = Berry(screen, BLOCK_SIZE, snake)
            
        elif cannibal:
            print("you lost")
            # clear the screen or draw a sign onto the screen
            break

        tail = SnakeTile(snake.array[0].screen, (snake.array[0].top, snake.array[0].left), snake.array[0].width)

        pygame.display.flip()

if __name__ == '__main__':
    main()
