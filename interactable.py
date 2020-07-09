from pygame import Rect
import utils


class Fluid(object):

    def __init__(self, typ=0, x_left=None, y_top=None, width=1, height=.7):
        self.typ = typ  # 0 = Wasser, 1 = Elektrizität, 2 = Säure
        y_top = y_top + .2
        self.rect = Rect(x_left * 25, y_top * 25, width * 25, height * 25)
        if typ == 0:
            self.color = (0, 255, 255)
        elif typ == 1:
            self.color = (255, 255, 0)
        else:
            self.color = (0, 255, 0)


class Button(object):

    def __init__(self, tag=None, x_left=None, y_top=None, width=1, height=.3):
        self.tag = tag
        self.pressed = False
        self.flow_pressed = False
        self.press_speed = 0
        self.y_top = (y_top + 1 - height) * 25
        self.rect = Rect(x_left * 25, self.y_top, width * 25, height * 25)
        self.color = (0, 100, 100)

    def update(self, dt):
        if self.pressed:
            self.rect.y += self.press_speed * dt
        else:
            self.rect.y -= self.press_speed * dt
        self.rect.top = utils.clamp(self.rect.top, self.y_top + self.rect.height * 2 / 3, self.y_top)


class Door(object):

    def __init__(self, tag=None, x_left=None, y_top=None, width=.5, height=2.5, target_height=0):
        self.tag = tag
        self.velY = .2
        self.open = False
        self.y_top = y_top * 25
        self.target_height = (target_height + y_top) * 25
        self.rect = Rect(x_left * 25, self.y_top, width * 25, height * 25)
        self.color = (0, 100, 100)

    def update(self, dt):
        if self.open:
            if self.target_height - self.y_top < 0:
                self.velY = -.2
            elif self.target_height - self.y_top > 0:
                self.velY = .2
            if self.velY > 0 and self.rect.top >= self.target_height:
                self.velY = 0
                self.rect.top = self.target_height
            if self.velY < 0 and self.rect.top <= self.target_height:
                self.velY = 0
                self.rect.top = self.target_height
        else:
            if self.target_height - self.y_top < 0:
                self.velY = .2
            elif self.target_height - self.y_top > 0:
                self.velY = -.2
            if self.velY > 0 and self.rect.top >= self.y_top:
                self.velY = 0
                self.rect.top = self.y_top
            if self.velY < 0 and self.rect.top <= self.y_top:
                self.velY = 0
                self.rect.top = self.y_top

        self.rect.y += self.velY * dt
