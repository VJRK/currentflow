import pygame
import globalvalues as gv
import utils

posX = 600 * gv.scale
posY = 450 * gv.scale
velX = 0
velY = 0
accX = 0


def handleinput(self, event):
    # Taste gedrückt
    if event.type == pygame.KEYDOWN:
        # A (links)
        if event.key == pygame.K_a:
            self.accX += -0.0025
        # D (rechts)
        elif event.key == pygame.K_d:
            self.accX += 0.0025
        # W (springen)
        elif event.key == pygame.K_w:
            self.velY = -1
    # Taste losgelassen
    elif event.type == pygame.KEYUP:
        # A (links)
        if event.key == pygame.K_a:
            self.accX += 0.0025
        # D (rechts)
        elif event.key == pygame.K_d:
            self.accX += -0.0025


def update(self, dt):
    self.posX += self.velX * dt * gv.scale
    self.posX = utils.clamp(self.posX, gv.width - gv.hitbox_cu[0] / 2, gv.hitbox_cu[0] / 2)

    self.posY += self.velY * dt * gv.scale
    self.posY = utils.clamp(self.posY, gv.height - gv.hitbox_cu[1] / 2, gv.hitbox_cu[1] / 2)

    self.velX += self.accX * dt
    self.velX *= gv.friction

    self.velY += gv.gravity * dt


def render(window):
    pygame.draw.rect(window, (0, 255, 255), (gv.L + posX - gv.hitbox_cu[0] / 2, gv.T + posY - gv.hitbox_cu[1] / 2,
                                             gv.hitbox_cu[0], gv.hitbox_cu[1]))
