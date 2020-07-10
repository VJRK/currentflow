import pygame
from collision import *


class Player:
    def __init__(self, is_flow, pos_x=0, pos_y=0, color=(255, 0, 0)):
        self.is_flow = is_flow
        self.dead = False
        self.has_jump = True
        self.width = int(gv.width / 80)
        self.height = int(gv.width / 60)
        self.posX = pos_x
        self.posY = pos_y
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.color = color

    def handleinput(self, event):

        if event.type == pygame.KEYDOWN:

            # links (A für current, LEFT für flow)
            if (self.is_flow and event.key == pygame.K_LEFT) \
                    or (not self.is_flow and event.key == pygame.K_a):
                self.accX = -gv.run_acc

            # rechts (D für current, RIGHT für flow)
            if (self.is_flow and event.key == pygame.K_RIGHT) \
                    or (not self.is_flow and event.key == pygame.K_d):
                self.accX = gv.run_acc

            # springen (W für current, UP für flow)
            if (self.is_flow and event.key == pygame.K_UP) \
                    or (not self.is_flow and event.key == pygame.K_w):
                if self.has_jump:
                    jumppower = (2 * gv.gravity * gv.jumpHeight) ** (1 / 2)
                    self.velY = -jumppower
                    self.has_jump = False

        # Stillstand wenn weder links noch rechts gedrückt wird
        key = pygame.key.get_pressed()
        if (self.is_flow and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT])\
                or (not self.is_flow and not key[pygame.K_a] and not key[pygame.K_d]):
            self.accX = 0

    def update(self, dt, stage):
        # self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        # X
        self.posX += self.velX * dt
        self.velX += self.accX * dt
        self.velX *= gv.frictionGround
        self.velX = utils.clamp(self.velX, gv.velXmaxGround, -gv.velXmaxGround)

        # Horizontale Kollision
        horizontal_collisions(self, stage.blocks)
        horizontal_door_collisions(self, stage.interactables)

        # Y
        self.posY += self.velY * dt
        self.velY += gv.gravity * dt
        self.velY = utils.clamp(self.velY, gv.velYmaxDown, gv.velYmaxUp)

        # Vertikale Kollision
        vertical_collisions(self, stage.blocks)
        vertical_door_collisions(self, stage.interactables)

        # Rampenkollision
        ramp_collisions(self, stage.blocks)

        # Kollision mit Interactables
        fluid_collisions(self, stage.interactables)
        button_collisions(self, stage.interactables)

        # c.check_door_collisions(self, Door.instances)
        # c.check_button_collision(self, Button.instances, Door.instances)

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.posX - self.width / 2, self.posY - self.height / 2,
                                              self.width, self.height))
