import pygame
import random
import datetime
import sys
import time

import update_json
from constants import *

grid = []

def prepare_grid():
    for row in range(100):
        grid.append([])

        for column in range(100):
            if column < 15 or column > 20:
                grid[row].append(1)
            else:
                grid[row].append(0)

def display_image(game_display, car_image, x, y):
    game_display.blit(car_image, (x, y))

# Setup Game
prepare_grid()
pygame.init()

def run_car(object, x, y, accident_type):
    pygame.display.set_caption("Car Simulation")

    car_image = pygame.image.load("utils/Car.png")
    car_image = pygame.transform.scale(car_image, CAR_SIZE)

    obstacles = []
    if (accident_type == CRASHED):
        lat = [600, 700, 650]
        lon = [400, 245, 72]
        for i in range(1, 4) :
            filename = f"utils/Obstacle_{i}.png"
            obstacle = pygame.image.load(filename)
            obstacle = pygame.transform.scale(obstacle, OBSTACLE_SIZE)

            obstacles.append((obstacle, lat[i - 1], lon[i - 1]))

    game_display = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    boom = pygame.image.load("utils/Boom.png")
    boom = pygame.transform.scale(boom, (90, 130))

    crashed = [False] * 3
    for i in range(len(object.movements)):
        for row in range(100):
            for column in range(100):
                color = WHITE

                if grid[row][column] == 1:
                    color = BLACK
                
                pygame.draw.rect(game_display, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                 WIDTH, HEIGHT])            

        display_image(game_display, car_image, object.x, object.y)

        for j in range(len(obstacles)):
            obstacle, latitude, longitude = obstacles[j]
            display_image(game_display, obstacle, latitude, longitude)

            # If the manhattan distance is less or equal than 50 units, we assume that the car has crashed the obstacles
            if abs(latitude - object.x) + abs(longitude - object.y) <= 50 and not crashed[j]:
                display_image(game_display, boom, latitude, longitude)

                crashed[j] = True
                update_json.is_crashed(object)

        object.x -= object.movements[i]
        object.y -= 10

        # Based on the random generated movement, we can assume that if i is equal to 40 and the type is `squiggly`, it is guaranteed that it moves in an improper way
        if i == 40 and accident_type == SQUIGGLY:
            update_json.is_squiggly(object)

        clock.tick(20)
        pygame.display.flip()

    pygame.quit()