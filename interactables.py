import pygame
import globalvalues as gv
import barriers as b


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
                pygame.draw.rect(window, (255, 255, 0), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))
            elif fluid.typ == "water":
                pygame.draw.rect(window, (0, 255, 255), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))
            elif fluid.typ == "acid":
                pygame.draw.rect(window, (0, 255, 0), (gv.L + fluid.rect[0], gv.T + fluid.rect[1], fluid.rect[2], fluid.rect[3]))


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
        self.y_top = (y_top + 1.05 - height) * s
        self.rect = pygame.Rect(x_left * s, self.y_top, width * s, height * s)

    def update(self, dt):
        if self.pressed:
            if self.rect.height - 2 > self.rect.top - self.y_top:
                self.rect.y += self.press_speed * dt
        else:
            if self.rect.top > self.y_top:
                self.rect.y -= self.press_speed * dt


    @staticmethod
    def render(window):
        for button in Button.instances:
            pygame.draw.rect(window, (0, 100, 100), (gv.L + button.rect[0], gv.T + button.rect[1], button.rect[2], button.rect[3]))


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
        Door.instances.append(self)
        s = gv.scale * 25
        self.y_top = y_top * s
        self.rect = pygame.Rect(x_left * s, self.y_top, width * s, height * s)

    def update(self, dt):
        print(self.open)
        if self.open:
            print(self.rect.bottom, self.y_top + self.rect.height)
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
            pygame.draw.rect(window, (0, 100, 100), (gv.L + door.rect[0], gv.T + door.rect[1], door.rect[2], door.rect[3]))
