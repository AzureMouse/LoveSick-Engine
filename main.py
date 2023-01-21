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
from text import *
# Initalize pygame
pygame.init()

# Various instances
image_instance = Image()
win_instance = Window()
text_instance = Text()

# Colors
BLACK = 0, 0, 0
text = "... I got to meet you again. Welcome back."

image_instance.set_background("background.jpg")
text_instance.set_current_player("Marie" + ":") # Set the current player

text_instance.set_dialog(text) # -> Set the dialog

current_character = text_instance.get_current_player() # -> Fetch current player
message = text_instance.get_dialog()

font = text_instance.get_font() # Fetch the font

window = pygame.display.set_mode((win_instance.get_width(), win_instance.get_height()))

is_running = True

background = image_instance.get_background()
new_size = pygame.transform.scale(background, (win_instance.get_width(), win_instance.get_height()))

character = text_instance.get_current_player()

# Draw
def draw():
    window.blit(new_size, (0, 0))
    text_instance.render_player(window, current_character)
    text_instance.render_text(window, message) 
    
    pygame.display.flip()

while(is_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        draw()

        pygame.display.flip()
