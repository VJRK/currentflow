from block import *
from interactable import *
from level import *
import random
import pygame.freetype

# Das Freetype-Modul initialisieren
pygame.freetype.init()

all_levels = [[level1], [level2], [level3],[level4],[level5]]
blocks = []
wall_variations = []
interactables = []
posCurrent = (0, 0)
posFlow = (0, 0)

# "Verlassen"-Schriftzug in der oberen rechten Ecke
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)
text_surface, rect2 = FONT_SD.render("Verlassen", (0, 255, 255, 100))
text_rect = pygame.Rect(gv.width * 46 / 50 - rect2[2] / 2, gv.height * 1 / 18 - rect2[3] / 2, rect2[2], rect2[3])
backspace = pygame.transform.scale(pygame.image.load('tasten/backspace.png'), (int(gv.width / 18), int(gv.width / 34)))

w_img1 = pygame.transform.scale(pygame.image.load("wall_images/wand1.png"), (gv.sc, gv.sc))
w_img2 = pygame.transform.scale(pygame.image.load("wall_images/wand2.png"), (gv.sc, gv.sc))
w_img3 = pygame.transform.scale(pygame.image.load("wall_images/wand3.png"), (gv.sc, gv.sc))
ramp_r_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_r.png"), (gv.sc, gv.sc))
ramp_l_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_l.png"), (gv.sc, gv.sc))
all_wall_imgs = [w_img1, w_img2, w_img3]


def build_level(self, index):
    self.blocks = []
    self.interactables = []
    self.wall_variations = []
    x = 0
    y = 0
    for row in all_levels[index][0]:
        for char in row:
            if char == "e": #Strom
                interactables.append(Fluid(1, x, y))
            elif char == "è": #Strom+RampeLinks
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(2, x, y))
            elif char == "ê": #Strom+Boden
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "é": #Strom+RampeRechts
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(1, x, y))
            elif char == "w": #Wasser
                interactables.append(Fluid(0, x, y))
            elif char == "ú": #Wasser+RampeRechts
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(1, x, y))
            elif char == "u": #Wasser+Boden
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "ù": #Wasser+RampeLinks
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(2, x, y))
            elif char == "a": #Säure
                interactables.append(Fluid(2, x, y))
            elif char == "A": #Säure mit Boden
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "Ä": #Säure+RampeLinks
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(2, x, y))
            elif char == "ä": #Säure+RampeRechts
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(1, x, y))
            elif char == "W":
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
                #Wand nach unten versetzt
                blocks.append(Block(0, x, y + .7, height=.3))
            elif char == "c":
                # Rampe rechts + nach unten versetzte Wand
                blocks.append(Block(0, x, y + .7, height=.3))
                blocks.append(Block(1, x, y))
            elif char == "C":
                print(x)
                print(y)
                self.posCurrent = (x * gv.sc, y * gv.sc)
            elif char == "F":
                self.posFlow = (x * gv.sc, y * gv.sc)

            elif char == " ":
                continue
            elif char == "1":
                interactables.append(Button(1, x, y, activated_by=1))
            elif char == "2": # horizontal up
                interactables.append(Door(1, x, y + 0.5, height=0.5, width=2.5, target_height=-2))
            elif char == "6": # horizontal down
                interactables.append(Door(1, x, y + 0.5, height=0.5, width=2.5, target_height=2.5))
            elif char == "7": # vertikal down
                interactables.append(Door(1, x + 0.25, y - 4, height=5, target_height=5.5))
            elif char == "8": # vertikal up
                interactables.append((Door(1, x + 0.25, y - 4, height=5, target_height=-5.5)))
            elif char == "3":
                interactables.append(Button(2, x, y, activated_by=2))
            elif char == "4": # vertikal down
                interactables.append(Door(2, x + 0.25, y - 4, height=5, target_height=5.5))
            elif char == "9": # vertikal up
                interactables.append((Door(2, x + 0.25, y - 4, height=5, target_height=-5.5)))
            elif char == "5":# horizontal up
                interactables.append(Door(2, x, y + .5, height=.5, width=2.5, target_height=-2))
            elif char == " ":
                continue
            self.wall_variations.append(random.randint(0, len(all_wall_imgs) - 1))
            x += 1
        y += 1
        x = 0

    x = 0
    y = 0


def update(dt):
    # Knöpfe und Türen updaten
    for inter in interactables:
        if inter.__class__ == Button or inter.__class__ == Door:
            inter.update(dt)


def render(self, canvas):

    # Alle Interactables rendern
    for inter in interactables:
        pygame.draw.rect(canvas, inter.color, (inter.rect.x, inter.rect.y, inter.rect.width, inter.rect.height))

    # Alle Blöcke des Levels rendern
    i = 0
    for block in self.blocks:

        # Rechteckige Blöcke
        if block.typ == 0:  # Wand
            canvas.blit(all_wall_imgs[wall_variations[i]], (block.rect.x, block.rect.y))
            i += 1

        # Rampen in Form von Polygonen anhand des Rechtecks
        elif block.typ == 1:  # RampeR
            canvas.blit(ramp_r_img, (block.rect.x, block.rect.y))
        elif block.typ == 2:  # RampeL
            canvas.blit(ramp_l_img, (block.rect.x, block.rect.y))

    # Verlassen
    canvas.blit(text_surface, text_rect)
    # Backspace
    canvas.blit(backspace, (gv.width * 92 / 100, gv.height * 8 / 100))
