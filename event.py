import numpy as np
import pygame


class GameEvent():
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

def set_allowed_event():
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.quit])

def events():
    closed = False
    quit = False

    for event in pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True


    return {"quit_to_main_menu":quit,
            "closed":closed,
            "clicked":pygame.mouse.get_pressed(),
            "mouse_pos": np.array(pygame.mouse.get_pos())}