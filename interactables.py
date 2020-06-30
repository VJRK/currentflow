import pygame
import globalvalues as gv
import barriers as b
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
        self.rect = pygame.Rect(x_left * gv.scale, y_top * gv.scale, width * gv.scale, height * gv.scale)

    @staticmethod
    def render(window):
        for fluid in Fluid.instances:
            if fluid.typ == "electricity":
                pygame.draw.rect(window, (255, 255, 0), (fluid.rect.x, fluid.rect.y, fluid.rect.width, fluid.rect.height))
            elif fluid.typ == "water":
                pygame.draw.rect(window, (0, 255, 255), (fluid.rect.x, fluid.rect.y, fluid.rect.width, fluid.rect.height))
            elif fluid.typ == "acid":
                pygame.draw.rect(window, (0, 255, 0), (fluid.rect.x, fluid.rect.y, fluid.rect.width, fluid.rect.height))


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
        self.y_top = math.ceil((y_top + 1 - height) * gv.scale)
        self.rect = pygame.Rect(x_left * gv.scale, self.y_top, width * gv.scale, height * gv.scale)

    def update(self, dt):
        if self.pressed:
            if self.rect.top < self.y_top + self.rect.height - max((self.rect.height/3), 2):
                self.rect.y += self.press_speed * dt
        else:
            if self.rect.top > self.y_top:
                self.rect.y -= self.press_speed * dt


    @staticmethod
    def render(window):
        for button in Button.instances:
            pygame.draw.rect(window, (0, 100, 100), (button.rect.x, button.rect.y, button.rect.width, button.rect.height))


class Door:
    instances = []

    def __init__(self,
                 tag=None,
                 x_left=None,
                 y_top=None,
                 width=.5,
                 height=2):
        self.tag = tag
        self.open = False
        self.stuck = False
        Door.instances.append(self)
        self.y_top = y_top * gv.scale
        self.rect = pygame.Rect(x_left * gv.scale, self.y_top, width * gv.scale, height * gv.scale)

    def update(self, dt):
        print(self.open, self.stuck)
        if self.open:
            if self.rect.bottom > self.y_top:
                self.rect.y -= .2 * dt
        else:
            if self.rect.top < self.y_top:
                self.rect.y += .2 * dt
            elif self.rect.top > self.y_top:
                self.rect.y = self.y_top

    @staticmethod
    def render(window):
        for door in Door.instances:
            pygame.draw.rect(window, (0, 100, 100), (door.rect.x, door.rect.y, door.rect.width, door.rect.height))
