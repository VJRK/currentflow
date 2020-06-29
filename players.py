import pygame
import globalvalues as gv
import collisions
from barriers import Barrier


class Current:
    def __init__(self,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        s = gv.scale * 25
        self.posX = x_left * s
        self.posY = y_top * s
        self.hitbox = (width * s, height * s)
        self.rect = pygame.Rect(self.posX, self.posY, self.hitbox[0], self.hitbox[1])
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.velX = 0
        self.accX = 0
        self.velY = 0

    def handleinput(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.velX = -gv.base_speed
            self.accX = -gv.run_acc
        if key[pygame.K_d]:
            self.velX = gv.base_speed
            self.accX = gv.run_acc
        if key[pygame.K_w]:
            if self.collision_types['bottom']:
                self.velY = -gv.jump_speed
        if not key[pygame.K_d] and not key[pygame.K_a]:
            self.velX = 0
            self.accX = 0

    def update(self, dt):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        if abs(self.velX) <= gv.max_speed:
            self.velX += self.accX * dt
        self.rect.x += self.velX * dt

        collides = collisions.check_collisions(self.rect, Barrier.instances)
        for collide in collides:
            if self.velX > 0:
                self.rect.right = collide.rect.left
                self.velX = 0
                self.collision_types['right'] = True
            elif self.velX < 0:
                self.rect.left = collide.rect.right
                self.velX = 0
                self.collision_types['left'] = True

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt

        collides = collisions.check_collisions(self.rect, Barrier.instances)
        for collide in collides:
            if self.velY > 0:
                self.rect.bottom = collide.rect.top
                self.velY = 0
                self.collision_types['bottom'] = True
            elif self.velY < 0:
                self.rect.top = collide.rect.bottom
                self.velY = 0
                self.collision_types['top'] = True

    def render(self, window):
        pygame.draw.rect(window, (255, 255, 0), (self.rect.x, self.rect.y, self.hitbox[0], self.hitbox[1]))


class Flow:
    def __init__(self,
                 x_left=None,
                 y_top=None,
                 width=1,
                 height=1):
        s = gv.scale * 25
        self.posX = x_left * s
        self.posY = y_top * s
        self.hitbox = (width * s, height * s)
        self.rect = pygame.Rect(self.posX, self.posY, self.hitbox[0], self.hitbox[1])
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.velX = 0
        self.accX = 0
        self.velY = 0

    def handleinput(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.velX = -gv.base_speed
            self.accX = -gv.run_acc
        if key[pygame.K_RIGHT]:
            self.velX = gv.base_speed
            self.accX = gv.run_acc
        if key[pygame.K_UP]:
            if self.collision_types['bottom']:
                self.velY = -gv.jump_speed
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
            self.velX = 0
            self.accX = 0

    def update(self, dt):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        if abs(self.velX) <= gv.max_speed:
            self.velX += self.accX * dt
        self.rect.x += self.velX * dt

        collides = collisions.check_collisions(self.rect, Barrier.instances)
        for collide in collides:
            if self.velX > 0:
                self.rect.right = collide.rect.left
                self.velX = 0
                self.collision_types['right'] = True
            elif self.velX < 0:
                self.rect.left = collide.rect.right
                self.velX = 0
                self.collision_types['left'] = True

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt

        collides = collisions.check_collisions(self.rect, Barrier.instances)
        for collide in collides:
            if self.velY > 0:
                self.rect.bottom = collide.rect.top
                self.velY = 0
                self.collision_types['bottom'] = True
            elif self.velY < 0:
                self.rect.top = collide.rect.bottom
                self.velY = 0
                self.collision_types['top'] = True

    def render(self, window):
        pygame.draw.rect(window, (0, 255, 255), (self.rect.x, self.rect.y, self.hitbox[0], self.hitbox[1]))
