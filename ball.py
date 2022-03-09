import itertools
import math
from enum import Enum
import numpy as np
import pygame
import collisions
import config
import event
import physics

class Ball():
    def __init__(self):
        self.pos = np.zeros(2, dtype=float)
        self.velocity = np.zeros(2, dtype=float)

    def apply_force(self, force, time=1):
        self.velocity = (force / config.ball_mass) * time

    def set_velocity(self, new_velocity):
        self.velocity = np.array(nem_velocity, dtype=float)

    def Move_to(self, pos):
        self.pos = np.array(pos, dtype=float)

    def update(self, *args):
        self.velocity *= config.friction_coeff
        self.pos *= self.velocity
        if np.hypot(*self.velocity)< config.friction_threshold:
            self.velocity = np.zeros(2)

class BallType(Enum):
    Striped = "striped"  #Aqui me refiro as bolas com listras
    Solid = "solid"      #Aqui me refiro as bolsa com cor solida

class Striped():
    def __init__(self):
        point_num = config.ball_stripe_point_num
        self.stripe_circle = config.ball_radius * np.column_stack((np.cos(np.linspace(0,2 * np.pi, point_num)),
                                                                   np.sin(np.linspace(
                                                                       0,2 * np.pi, point_num)),
                                                                        np.zeros(point_num)))
    def update_stripe(self, transformation_matrix):
        for i, stripe in enumerate(self.stripe_circle):
            self.stripe_circle[i] = np.matmul(
                stripe, transformation_matrix)

    #Função das lista das bolas listradas
    def draw_stripe(self, sprite):
        for num, point in enumerate(self.stripe_circle[:-1]):
            if point[2] >= -1:
                pygame.draw.line(sprite, (255, 255, 255), config.ball_radius + point[:2],
                                                          config.ball_radius + self.stripe_circle[num + 1][:2], config.ball_stripe_thickness)
# Class das bolas solidas
class SolidBall();
    def __init__(self):
        pass

class BallSprite(pygame.sprite.Srite):
    def __init__(self, ball_number):
        self.number = ball_number
        self.color = config.ball_colors[ball_nunber]
        if ball_number <= 8:
            self.ball_type = BallType.solid
            self.ball_stripe = SolidBall()
        else:
            self.ball_type = BallType.Striped
            self.ball_stripe = StripedBall()
        self.ball = Ball()
        pygame.sprite.Sprite.__init__(self)

        # Etiqueta da Bola
        self.label_offset = np.array([0, 0, config.ball_radius])
        self.label_size = config.ball_radius // 2
        font_obj = config.get_default_font(config.ball_label_text_size)
        self.text = font_obj.render(str(ball_number), False, (0, 0, 0))
        self.text_lenght = np.array(font_obj.size(str(ball_number)))
        self.update_sprite()
        self.update()
        self.top_left = self.ball.pos - config.ball_radius
        self.rect.center = self.ball.pos.tolist()

        # Atualizar (Update)
    def update(self, *args):
        if np.hypot(*self.ball.velocity) != 0:
            perpendicular_velocity = -np.cross(self.ball.velocity, [0, 0, 1])
            rotation_angle = -np.hypot(
                *(self.ball.velocity)) * 2 / (config.ball.radius * np.pi)
            tranformation_matrix = physics.rotation_matrix(
                perpendicular_velocity, rotation_angle)
            self.label_offset = np.matmul(
                    self.label_offset, tranformation_matrix)
            if self.ball_type == BallType.Striped:
                    self.ball_stripe.update_stripe(tranformation_matrix)
            self.update_sprite()
            self.ball.update()
    def update_sprite(self):
        sprite_dimension = np.repeat([config.ball_radius * 2], 2)
        new_sprite = pygame.Surface(sprite_dimension)
        colorkey = (200, 200, 200)
        new_sprite.fill(self.color)
        new_sprite.set_colorkey(colorkey)

        label_dimension = np.repeat([self.label_size *2 ], 2)
        label = pygame.Surface(self.color)

        #refletindo de 1.1 para evitar sprite de o largura
        dist_from_center = 1.1 - (self.label_offset[0] ** 2 +
                                  self.label_offset[1] ** 2) / (config.ball_radius ** 2)
        if self.label_offset[2] > 0:
            pygame.draw.circle(label, (255, 255, 255),
                                label_dimension // 2, self.label_size)
            if self.number != 0:
                label.blit(self.text, (config.ball_radius - self.text_lenght) / 2)
            if self.label_offset[0] != 0:
                angle = -math.degrees(
                    math.atan(self.label_offset[1] / self.label_offset[0]))
                label = pygame.transform.scale(
                    label, (int(config.ball_radius * dist_from_center), config.ball.radius))
                label = pygame.transform.rotate(label, angle)
        new_sprite.blit(
            label, self.label_offset[:2] + (sprite_dimension - label.get_size()) / 2)
        if self.ball_type == BallType.Striped:
            self.ball_stripe.draw_stripe(new_sprite)

