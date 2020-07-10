from block import *
from interactable import *
from level import *


all_levels = [[level1_b, level1_i], [level2, level2_i]]
blocks = []
interactables = []
posCurrent = (0, 0)
posFlow = (0, 0)
# Basic_Wall_IMG = pygame.image.load("Wall_Images/BlueWallFull.png")
# Ramp_Right_IMG = pygame.image.load("Wall_Images/RampRight.png")
# Ramp_Left_IMG = pygame.image.load("Wall_Images/RampLeft.png")
Basic_Wall_IMG = pygame.image.load("tasten/w.png")
Ramp_Right_IMG = pygame.image.load("tasten/d.png")
Ramp_Left_IMG = pygame.image.load("tasten/a.png")


def build_level(self, index):
    self.blocks = []
    self.interactables = []
    x = 0
    y = 0
    for row in all_levels[index][0]:
        for char in row:
            if char == "W":
                blocks.append(Block(0, x, y))
            elif char == "T":
                blocks.append(Block(0, x, y, height=.5))
            elif char == "B":
                blocks.append(Block(0, x, y + .5, height=.5))

            elif char == "R":
                blocks.append(Block(1, x, y))
            elif char == "L":
                blocks.append(Block(2, x, y))
            elif char == "Ṙ":
                blocks.append(Block(1, x, y))
                blocks.append(Block(3, x + 1.001, y + .01, height=.0001, width=.0001))
            elif char == "Ḷ":
                blocks.append(Block(2, x, y))
                blocks.append(Block(3, x, y + .01, height=.0001, width=.0001))

            elif char == "b":
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "a":
                blocks.append(Block(0, x, y, width=.5))
                blocks.append(Block(2, x + .5, y))
            elif char == "c":
                blocks.append(Block(0, x, y + .7, height=.3))
                blocks.append(Block(1, x, y))

            elif char == "C":
                self.posCurrent = (x * gv.sc, y * gv.sc)
            elif char == "F":
                self.posFlow = (x * gv.sc, y * gv.sc)

            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0

    x = 0
    y = 0
    for row in all_levels[index][0]:
        for char in row:
            if char == "w":
                interactables.append(Fluid(0, x, y))
            elif char == "e":
                interactables.append(Fluid(1, x, y))
            elif char == "a":
                interactables.append(Fluid(2, x, y))

            elif char == "1":
                interactables.append(Button(1, x, y, activated_by=1))
            elif char == "2":
                interactables.append(Door(1, x, y + 0.5, height=0.5, width=2.5, target_height=-2))
            elif char == "3":
                interactables.append(Button(2, x, y, activated_by=2))
            elif char == "4":
                interactables.append(Door(2, x + 0.25, y - 4, height=5, target_height=5.5))
            elif char == "5":
                interactables.append(Door(2, x, y + .5, height=.5, width=2.5, target_height=-2))
            elif char == " ":
                continue
            x += 1
        y += 1
        x = 0


def update(dt):
    # Knöpfe und Türen updaten
    for inter in interactables:
        if inter.__class__ == Button or inter.__class__ == Door:
            inter.update(dt)


def render(self, window):

    # Alle Interactables rendern
    for inter in interactables:
        pygame.draw.rect(window, inter.color, (inter.rect.x, inter.rect.y, inter.rect.width, inter.rect.height))

    # Alle Blöcke des Levels rendern
    for block in self.blocks:

        # Rechteckige Blöcke
        if block.typ == 0:  # Wand
            window.blit(pygame.transform.scale(Basic_Wall_IMG, (block.rect.width, block.rect.height)),
                        (block.rect.x, block.rect.y))

        # Rampen in Form von Polygonen anhand des Rechtecks
        elif block.typ == 1:  # RampeR
            window.blit(pygame.transform.scale(Ramp_Right_IMG, (block.rect.width, block.rect.height)),
                        (block.rect.x, block.rect.y))
        elif block.typ == 2:  # RampeL
            window.blit(pygame.transform.scale(Ramp_Left_IMG, (block.rect.width, block.rect.height)),
                        (block.rect.x-1, block.rect.y))
