import pygame
import globalvalues as gb

posX = 10 * gb.scale
posY = 10 * gb.scale
velX = 0
velY = 0
accX = 0
accY = 0


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
            self.accY = -0.05
    # Taste losgelassen
    elif event.type == pygame.KEYUP:
        # A (links)
        if event.key == pygame.K_a:
            self.accX += 0.0025
        # D (rechts)
        elif event.key == pygame.K_d:
            self.accX += -0.0025


def update(self, dt):
    self.posX += self.velX * dt
    self.posY += self.velY * dt
    self.velX += self.accX * dt
    self.velY += self.accY * dt


def render(window):
    pygame.draw.rect(window, (0, 255, 255), (posX - 32, posY - 32, 64, 64))
