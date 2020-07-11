import pygame
from math import fabs
from collision import *


class Player:
    def __init__(self, is_flow, pos_x=0, pos_y=0, color=(255, 0, 0)):
        self.is_flow = is_flow
        self.dead = False
        self.has_jump = True
        self.width = 24
        self.height = 32
        self.posX = pos_x
        self.posY = pos_y
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.color = color
        self.delta = 0
        self.sprites = []
        if self.is_flow:
            sprites = [pygame.image.load("characters/flow/stand.png"),
                       pygame.image.load("characters/flow/stand_left.png"),
                       pygame.image.load("characters/flow/stand_right.png"),
                       pygame.image.load("characters/flow/jump_left.png"),
                       pygame.image.load("characters/flow/jump_right.png"),
                       pygame.image.load("characters/flow/run_left1.png"),
                       pygame.image.load("characters/flow/run_left2.png"),
                       pygame.image.load("characters/flow/run_left3.png"),
                       pygame.image.load("characters/flow/run_right1.png"),
                       pygame.image.load("characters/flow/run_right2.png"),
                       pygame.image.load("characters/flow/run_right3.png")]
        else:
            sprites = [pygame.image.load("characters/flow/stand.png"),
                       pygame.image.load("characters/flow/stand_left.png"),
                       pygame.image.load("characters/flow/stand_right.png"),
                       pygame.image.load("characters/flow/jump_left.png"),
                       pygame.image.load("characters/flow/jump_right.png"),
                       pygame.image.load("characters/flow/run_left1.png"),
                       pygame.image.load("characters/flow/run_left2.png"),
                       pygame.image.load("characters/flow/run_left3.png"),
                       pygame.image.load("characters/flow/run_right1.png"),
                       pygame.image.load("characters/flow/run_right2.png"),
                       pygame.image.load("characters/flow/run_right3.png")]
        for sprite in sprites:
            self.sprites.append(pygame.transform.scale(sprite, (self.width, self.height)))
        del sprites

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
        if (self.is_flow and not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]) \
                or (not self.is_flow and not key[pygame.K_a] and not key[pygame.K_d]):
            self.accX = 0

    def update(self, dt, stage):
        if self.dead:
            stage.overlay = True

        # Vergangene Zeit für Laufanimation
        self.delta += dt

        # X
        self.posX += self.velX * dt
        self.velX += self.accX * dt
        self.velX *= gv.frictionGround
        if fabs(self.velX) < 0.001:
            self.velX = 0
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

    def render(self, canvas):

        # DEBUG
        pygame.draw.rect(canvas, (255, 0, 0), (self.posX - self.width / 2, self.posY - self.height / 2, self.width, self.height))

        i = 0  # enstpricht stehen

        # Wenn Spieler am Boden ist
        if self.has_jump:

            # Wenn Spieler nach links oder rechts drückt und langsam ist
            if self.accX != 0 and fabs(self.velX) <= 0.02:
                # Linksbewegung
                if self.accX < 0:
                    i = 1
                # Rechtsbewegung
                elif self.accX > 0:
                    i = 2

            # Laufen
            # Wenn Spieler nicht langsam ist
            elif fabs(self.velX) > 0.02:
                if self.velX < 0:

                    if self.delta < 60:
                        i = 5
                    elif self.delta < 120:
                        i = 6
                    else:
                        i = 7
                        if self.delta >= 180:
                            self.delta = 0

                elif self.velX > 0:

                    if self.delta < 60:
                        i = 8
                    elif self.delta < 120:
                        i = 9
                    else:
                        i = 10
                        if self.delta >= 180:
                            self.delta = 0

        # Wenn Spieler in der Luft ist
        else:
            if self.accX < 0:
                i = 3
            else:
                i = 4
        canvas.blit(self.sprites[i], (self.posX - self.width / 2, self.posY - self.height / 2,
                                      self.width, self.height))
