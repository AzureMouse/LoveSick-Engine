"""
File:       image.py
Project:    LoveSick Engine
Date:       1/17/23
Author:     AzureMouse
Description:
Handles game images
"""
import pygame

class Image:
    def __init__(self, background_image=None):
        self.background_image = background_image

    def set_background(self, image):
       self. background_image = pygame.image.load(image)

    def get_background(self):
        return  self.background_image

