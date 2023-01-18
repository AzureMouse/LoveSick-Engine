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

# Initalize pygame

pygame.init()
instance = Window()

# Colors
BLACK = 0, 0, 0

window = pygame.display.set_mode((instance.get_width(), instance.get_height()))

is_running = True

# Draw
def draw():
    window.fill(BLACK)
    window.blit("image.jpg")
    pygame.display.flip()

while(is_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        draw()
