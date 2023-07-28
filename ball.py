import pygame
import config as cfg
from math import sqrt, pow
from enum import Enum


class Moving(Enum):
    right = 1
    left = 2
    up = 3
    down = 4


class BallState:
    movement: (Moving, Moving)

    def __init__(self):
        self.movement = (Moving.right, Moving.up)


class Vec2:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, x2, y2) -> int:
        return round(sqrt(abs(pow(x2 - self.x, 2) + pow(y2 - self.y, 2))))


class Ball:
    pos: Vec2
    acc: int
    vel: Vec2
    radius: int
    color: (int, int, int)
    state: BallState

    def __init__(self):
        self.pos = Vec2(cfg.WIDTH / 2, cfg.HEIGHT / 2)
        self.acc = 1.0
        self.vel = 1.0
        self.direction = Vec2(1, 0)
        self.radius = 10
        self.color = (255, 255, 255)
        self.state = BallState()

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y),
                           self.radius)

    def update(self, x=0, y=0):
        dist = self.pos.distance_from(x, y)
        if dist >= 0:
            self.acc = dist / 100

            y_dist = y - self.pos.y
            self.direction.y = 1 if y_dist > 0 else 0 if y_dist == 0 else -1
            y_vel = (y_dist * 0.05) + self.acc * self.direction.y

            x_dist = x - self.pos.x
            self.direction.x = 1 if x_dist > 0 else 0 if x_dist == 0 else -1
            x_vel = (x_dist * 0.05) + self.acc * self.direction.x

            self.pos.x += x_vel
            self.pos.y += y_vel
        # if self.pos.x >= cfg.WIDTH or self.pos.x <= 0:
        #     self.vel.x *= -1
        # if self.pos.y >= cfg.HEIGHT or self.pos.y <= 0:
        #     self.vel.y *= -1
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
