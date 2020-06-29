import pygame
import globalvalues as gv
import utils

posX = 1000
posY = 450
velX = 0
velY = 0
accX = 0

hitbox = (64, 64)


def handleinput(self, event):
    # Taste gedrückt
    if event.type == pygame.KEYDOWN:
        # Linke Pfeiltaste (links)
        if event.key == pygame.K_LEFT:
            self.accX += -0.0025
        # Rechte Pfeiltaste (rechts)
        elif event.key == pygame.K_RIGHT:
            self.accX += 0.0025
        # Obere Pfeiltaste (springen)
        elif event.key == pygame.K_UP:
            self.velY = -1
    # Taste losgelassen
    elif event.type == pygame.KEYUP:
        # Linke Pfeiltaste (links)
        if event.key == pygame.K_LEFT:
            self.accX += 0.0025
        # Rechte Pfeiltaste (rechts)
        elif event.key == pygame.K_RIGHT:
            self.accX += -0.0025


def update(self, dt):
    self.posX += self.velX * dt
    self.posX = utils.clamp(self.posX, gv.width - hitbox[0] / 2, hitbox[0] / 2)

    self.posY += self.velY * dt
    self.posY = utils.clamp(self.posY, gv.height - hitbox[1] / 2, hitbox[1] / 2)

    self.velX += self.accX * dt
    self.velX *= gv.friction

    self.velY += gv.gravity * dt


def render(window):
    pygame.draw.rect(window, (255, 255, 0), (posX - hitbox[0] / 2, posY - hitbox[1] / 2, hitbox[0], hitbox[1]))
