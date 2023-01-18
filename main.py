"""
File:       main.py
Project:    LoveSick Engine
Date:       1/17/23
Description:
2D engine that will serve as the framework for visual novel games
"""

# Dependancies
import pygame
from window import *
from image import *

# Initalize pygame
pygame.init()

# Various instances
image_instance = Image()
win_instance = Window()

# Colors
BLACK = 0, 0, 0

image_instance.set_background("background.jpg")

window = pygame.display.set_mode((win_instance.get_width(), win_instance.get_height()))

is_running = True

background = image_instance.get_background()
new_size = pygame.transform.scale(background, (win_instance.get_width(), win_instance.get_height()))

# Draw
def draw():
    window.fill(BLACK)
    window.blit(new_size, (0, 0))
    pygame.display.flip()

while(is_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        draw()
