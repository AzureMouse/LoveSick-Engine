"""
File:       window.py
Project:    LoveSick Engine
Date:       1/17/23
Author:     AzureMouse
Description
Window and screen properties
"""
black = (0, 0, 0)

class Window:
    def __init__(self, width=1200, height=700):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


