import pygame
import globalvalues as gv
import math


class Fluid(object):
    instances = []

    def __init__(self,
                 typ=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=.7):
        self.typ = typ
        Fluid.instances.append(self)
        y_top = y_top + .2
        s = gv.scale * 25
        self.rect = pygame.Rect(x_left * s, y_top * s, width * s, height * s)

    @staticmethod
    def render(window):
        for fluid in Fluid.instances:
            if fluid.typ == "electricity":
                pygame.draw.rect(window, (255, 255, 0), (gv.L + fluid.rect.x, gv.T + fluid.rect.y,
                                                         fluid.rect.width, fluid.rect.height))
            elif fluid.typ == "water":
                pygame.draw.rect(window, (0, 255, 255), (gv.L + fluid.rect.x, gv.T + fluid.rect.y,
                                                         fluid.rect.width, fluid.rect.height))
            elif fluid.typ == "acid":
                pygame.draw.rect(window, (0, 255, 0), (gv.L + fluid.rect.x, gv.T + fluid.rect.y,
                                                       fluid.rect.width, fluid.rect.height))


class Button(object):
    instances = []

    def __init__(self,
                 tag=None,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=.3):
        self.tag = tag
        self.pressed = False
        self.who_pressed = None
        self.press_speed = 0
        Button.instances.append(self)
        s = gv.scale * 25
        self.y_top = math.ceil((y_top + 1 - height) * s)
        self.rect = pygame.Rect(x_left * s, self.y_top, width * s, height * s)

    def update(self, dt):
        if self.pressed:
            if self.rect.top < self.y_top + self.rect.height - max((self.rect.height / 3), 2):
                self.rect.y += self.press_speed * dt
        else:
            if self.rect.top > self.y_top:
                self.rect.y -= self.press_speed * dt

    @staticmethod
    def render(window):
        for button in Button.instances:
            pygame.draw.rect(window, (0, 100, 100), (gv.L + button.rect.x, gv.T + button.rect.y,
                                                     button.rect.width, button.rect.height))


class Door:
    instances = []

    def __init__(self,
                 tag=None,
                 x_left=None,
                 y_top=None,
                 width=.5,
                 height=2.5,
                 target_height=0):
        self.tag = tag
        self.velX = .2
        self.open = False
        Door.instances.append(self)

        s = gv.scale * 25
        self.y_top = y_top * s
        self.target_height = (target_height + y_top) * s
        self.rect = pygame.Rect(x_left * s, self.y_top, width * s, height * s)

    def update(self, dt):
        if self.open:
            if self.target_height - self.y_top < 0:
                self.velX = -.2
            elif self.target_height - self.y_top > 0:
                self.velX = .2
            if self.velX > 0 and self.rect.top >= self.target_height:
                self.velX = 0
                self.rect.top = self.target_height
            if self.velX < 0 and self.rect.top <= self.target_height:
                self.velX = 0
                self.rect.top = self.target_height
        else:
            if self.target_height - self.y_top < 0:
                self.velX = .2
            elif self.target_height - self.y_top > 0:
                self.velX = -.2
            if self.velX > 0 and self.rect.top >= self.y_top:
                self.velX = 0
                self.rect.top = self.y_top
            if self.velX < 0 and self.rect.top <= self.y_top:
                self.velX = 0
                self.rect.top = self.y_top

        self.rect.y += self.velX * dt

    @staticmethod
    def render(window):
        for door in Door.instances:
            pygame.draw.rect(window, (0, 100, 100), (gv.L + door.rect.x, gv.T + door.rect.y,
                                                     door.rect.width, door.rect.height))
