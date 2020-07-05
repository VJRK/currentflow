import pygame
import utils
import globalvalues as gv
from collision import *
from interactables import Fluid, Button, Door


class Player:
    def __init__(self, flow, pos_x=0, pos_y=0, color=(255, 0, 0)):
        self.flow = flow
        self.dead = False
        self.width = int(24 * gv.scale)
        self.height = int(32 * gv.scale)
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
            if (self.flow and event.key == pygame.K_LEFT) \
                    or (not self.flow and event.key == pygame.K_a):
                self.accX = -gv.run_acc

            # rechts (D für current, RIGHT für flow)
            if (self.flow and event.key == pygame.K_RIGHT) \
                    or (not self.flow and event.key == pygame.K_d):
                self.accX = gv.run_acc

            # springen (W für current, UP für flow)
            if (self.flow and event.key == pygame.K_UP) \
                    or (not self.flow and event.key == pygame.K_w):
                jumppower = (2 * gv.gravity * gv.jumpHeight * gv.scale) ** (1 / 2)
                self.velY = -jumppower

        # Stillstand wenn weder links noch rechts gedrückt wird
        key = pygame.key.get_pressed()
        if (self.flow and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT])\
                or (not self.flow and not key[pygame.K_a] and not key[pygame.K_d]):
            self.accX = 0

    def update(self, dt, stage):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.width = int(24 * gv.scale)
        self.height = int(32 * gv.scale)

        # X
        self.posX += self.velX * dt
        self.velX += self.accX * dt * gv.scale ** (1 / 2)
        self.velX *= gv.frictionGround
        self.velX = utils.clamp(self.velX, gv.velXmaxGround, -gv.velXmaxGround)

        # Horizontale Kollision
        self.posX = utils.clamp(self.posX, gv.width - self.width / 2, self.width / 2)
        horizontal_collisions(self, stage.blocks)

        # Y
        self.posY += self.velY * dt
        self.velY += gv.gravity * dt * gv.scale
        self.velY = utils.clamp(self.velY, gv.velYmaxDown, gv.velYmaxUp)

        # Horizontale Kollision
        self.posY = utils.clamp(self.posY, gv.height - self.height / 2, self.height / 2)
        vertical_collisions(self, stage.blocks)

        # update_collisions(self, stage.blocks)
        # c.check_door_collisions(self, Door.instances)
        # c.check_vertical_collisions(self, Barrier.instances)
        # c.check_ramp_collisions(self, Barrier.ramps)
        # c.check_horizontal_collisions(self, Barrier.instances)
        # c.check_fluid_collisions(self, Fluid.instances)
        # c.check_button_collision(self, Button.instances, Door.instances)
        # c.check_horizontal_collisions(self, Door.instances)

    def render(self, window):
        pygame.draw.rect(window, self.color, (gv.L + self.posX - self.width / 2, gv.T + self.posY - self.height / 2,
                                              self.width, self.height))
