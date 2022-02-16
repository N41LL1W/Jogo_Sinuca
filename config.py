import math
import numpy as np
import pygame

def get_default_font(size):
    font_default = pygame.font.get_default_font()
    return pygame.font.Font(font_default, size)

def set_max_resolution():
    infoObject = pygame.display.Info()
    global resolution()
    global white_ball_initial_pos
    resolution = np.array([infoObject.current_w, infoObject.current_h])
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, |0]) * [0.25, 0.5]

    fullscreaan = False

    if not fullscreen:
        resolution = np.array([1000, 500])
        window_caption = "Sinuca :"
        fps_limit = 60

        table_margin = 40
        table_side_color = (200, 200, 0)  #Define a cor da lateral da mesa
        table_color = (0, 100, 0) # Define a cor da mesa
        separation_line_color = (200, 200, 200)
        hole_radius = 22
        middle_hole_offset = np.array([[-hole_radius * 2, hole_radius], [-hole_radius,0],
                                       [hole_radius, 0], [hole_radius * 2, hole_radius]])
