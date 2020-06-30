import pygame
import globalvalues as gv
import collisions as c
from barriers import Barrier
from interactables import Fluid, Button, Door


class Current:
    def __init__(self,
                 name,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        self.name = name
        self.posX = x_left * gv.scale
        self.posY = y_top * gv.scale
        self.hitbox = (width * gv.scale, height * gv.scale)
        self.rect = pygame.Rect(self.posX, self.posY, self.hitbox[0], self.hitbox[1])
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.velX = 0
        self.accX = 0
        self.velY = 0
        self.color = (255, 255, 0)

    def handleinput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # A (links)
                self.velX = -gv.base_run_speed
                self.accX = -gv.run_acc
            if event.key == pygame.K_d:  # D (rechts)
                self.velX = gv.base_run_speed
                self.accX = gv.run_acc
            if event.key == pygame.K_w:  # W (springen)
                if self.collision_types['bottom']:
                    self.velY = -gv.jump_speed
        key = pygame.key.get_pressed()
        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.velX = 0
            self.accX = 0

    def update(self, dt):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt
        c.check_vertical_collisions(self, Barrier.instances)
        c.check_door_collisions(self, Door.instances)

        if abs(self.velX) <= gv.max_run_speed:
            self.velX += self.accX * dt
            self.color = (255, 255, 0)
        else:
            self.color = (100, 100, 0)
        self.rect.x += self.velX * dt
        c.check_ramp_collisions(self, Barrier.ramps)
        c.check_horizontal_collisions(self, Barrier.instances)
        c.check_fluid_collisions(self, Fluid.instances)
        c.check_button_collision(self, Button.instances)
        c.check_horizontal_collisions(self, Door.instances)

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.hitbox[0], self.hitbox[1]))


class Flow:
    def __init__(self,
                 name,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        self.name = name
        self.posX = x_left * gv.scale
        self.posY = y_top * gv.scale
        self.hitbox = (width * gv.scale, height * gv.scale)
        self.rect = pygame.Rect(self.posX, self.posY, self.hitbox[0], self.hitbox[1])
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.velX = 0
        self.accX = 0
        self.velY = 0
        self.color = (0, 255, 255)

    def handleinput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Linke Pfeiltaste (links)
                self.velX = -gv.base_run_speed
                self.accX = -gv.run_acc
            if event.key == pygame.K_RIGHT:  # Rechte Pfeiltaste (rechts)
                self.velX = gv.base_run_speed
                self.accX = gv.run_acc
            if event.key == pygame.K_UP:  # Obere Pfeiltaste (springen)
                if self.collision_types['bottom']:
                    self.velY = -gv.jump_speed
        key = pygame.key.get_pressed()
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            self.velX = 0
            self.accX = 0


    def update(self, dt):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt
        c.check_vertical_collisions(self, Barrier.instances)
        c.check_door_collisions(self, Door.instances)

        if abs(self.velX) <= gv.max_run_speed:
            self.velX += self.accX * dt
        self.rect.x += self.velX * dt
        c.check_ramp_collisions(self, Barrier.ramps)
        c.check_horizontal_collisions(self, Barrier.instances)
        c.check_fluid_collisions(self, Fluid.instances)
        c.check_button_collision(self, Button.instances)
        c.check_horizontal_collisions(self, Door.instances)

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y, self.hitbox[0], self.hitbox[1]))
