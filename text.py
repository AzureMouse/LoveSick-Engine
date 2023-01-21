"""
File:       text.py
Project:    LoveSick Engine
Date:       1/18/23
Author:     AzureMouse
Description:
Handles the text of the games
"""
import pygame

class Text:

    def __init__(self, text_counter=0, dialog=None, player="Zero", current_player=None):
        self.text_counter = text_counter
        self.dialog = dialog
        self.font = pygame.font.SysFont('arialblack', 32)
        self.player = player
        self.player_x = 200
        self.player_y = 550
        self.text_x = 300
        self.text_y = 600

    # Setters
    def set_text_counter(self, value):
        self.text_counter = value

    def set_dialog(self, value):
        self.dialog = value

    def set_font(self, value):
        self.font = value

    def set_current_player(self, player):
        self.current_player = player

    # Getters
    def get_text_counter(self):
        return self.text_counter

    def get_dialog(self):
        return self.dialog

    def get_font(self):
        return self.font

    def get_player_name(self):
        return self.player

    def get_current_player(self):
        return self.current_player
    
    # Render current character speaking
    def render_player(self, window, player):
        font = self.font
        message = font.render(player, False, (255, 255, 255))
        window.blit(message, (self.player_x, self.player_y))

    # Render current dialog for that character
    def render_text(self, window, text):
        font = self.font
        message = font.render(text, False, (255, 255, 255))
        window.blit(message, (self.text_x, self.text_y))
