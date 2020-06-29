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

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt * gv.scale

        collide_walls = collisions.check_collisions(self.rect, Barrier.instances)
        for collide_wall in collide_walls:
            if self.velY > 0:
                self.rect.bottom = collide_wall.rect.top
                self.velY = 0
                self.collision_types['bottom'] = True
            elif self.velY < 0:
                self.rect.top = collide_wall.rect.bottom
                self.velY = 0
                self.collision_types['top'] = True

        if abs(self.velX) <= gv.max_speed:
            self.velX += self.accX * dt
        self.rect.x += self.velX * dt * gv.scale

        collide_ramps = collisions.check_collisions(self.rect, Barrier.ramps)
        for collide_ramp in collide_ramps:
            rel_x = self.rect.x - collide_ramp.rect.x
            if collide_ramp.typ == "RampR":
                pos_height = rel_x + self.rect.width
            if collide_ramp.typ == "RampL":
                pos_height = 25 - rel_x
            pos_height = min(pos_height, 25)
            pos_height = max(pos_height, 0)
            target_y = collide_ramp.rect.y + 25 - pos_height
            if self.rect.bottom > target_y:
                self.rect.bottom = target_y
                self.velY = 0
                self.collision_types['bottom'] = True
            print(self.rect.bottom, target_y, rel_x)

        collide_walls = collisions.check_collisions(self.rect, Barrier.instances)
        for collide_wall in collide_walls:
            if self.velX > 0:
                self.rect.right = collide_wall.rect.left
                print("right wlall")
                self.velX = 0
                self.collision_types['right'] = True
            elif self.velX < 0:
                self.rect.left = collide_wall.rect.right
                self.velX = 0
                self.collision_types['left'] = True

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

        self.velY += gv.gravity * dt
        self.rect.y += self.velY * dt * gv.scale

        collide_walls = collisions.check_collisions(self.rect, Barrier.instances)
        for collide_wall in collide_walls:
            if self.velY > 0:
                self.rect.bottom = collide_wall.rect.top
                self.velY = 0
                self.collision_types['bottom'] = True
            elif self.velY < 0:
                self.rect.top = collide_wall.rect.bottom
                self.velY = 0
                self.collision_types['top'] = True

        if abs(self.velX) <= gv.max_speed:
            self.velX += self.accX * dt
        self.rect.x += self.velX * dt * gv.scale

        collide_ramps = collisions.check_collisions(self.rect, Barrier.ramps)
        for collide_ramp in collide_ramps:
            rel_x = self.rect.x - collide_ramp.rect.x
            if collide_ramp.typ == "RampR":
                pos_height = rel_x + self.rect.width
            if collide_ramp.typ == "RampL":
                pos_height = 25 - rel_x
            pos_height = min(pos_height, 25)
            pos_height = max(pos_height, 0)
            target_y = collide_ramp.rect.y + 25 - pos_height
            if self.rect.bottom > target_y:
                self.rect.bottom = target_y
                self.velY = 0
                self.collision_types['bottom'] = True
            print(self.rect.bottom, target_y, rel_x)

        collide_walls = collisions.check_collisions(self.rect, Barrier.instances)
        for collide_wall in collide_walls:
            if self.velX > 0:
                self.rect.right = collide_wall.rect.left
                print("right wlall")
                self.velX = 0
                self.collision_types['right'] = True
            elif self.velX < 0:
                self.rect.left = collide_wall.rect.right
                self.velX = 0
                self.collision_types['left'] = True

    def render(self, window):
        pygame.draw.rect(window, (0, 255, 255), (self.rect.x, self.rect.y, self.hitbox[0], self.hitbox[1]))
