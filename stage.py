from block import *
from interactable import *
from level import *
import random
import pygame.freetype

# Das Freetype-Modul initialisieren
pygame.freetype.init()

all_levels = [level1, level2, level3, level4, level5, level6]
selected_level = 0
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

# Sprites der Blöcke laden
w_img1 = pygame.transform.scale(pygame.image.load("wall_images/wand1.png"), (gv.sc, gv.sc))
w_img2 = pygame.transform.scale(pygame.image.load("wall_images/wand2.png"), (gv.sc, gv.sc))
w_img3 = pygame.transform.scale(pygame.image.load("wall_images/wand3.png"), (gv.sc, gv.sc))
w_img_halb = pygame.transform.scale(pygame.image.load("wall_images/wand_u.png"), (gv.sc, gv.sc))
ramp_r_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_r.png"), (gv.sc, gv.sc))
ramp_l_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_l.png"), (gv.sc, gv.sc))
all_wall_imgs = [w_img1, w_img2, w_img3]

# Sprites der Tasten laden und transparenter machen
taste_w = pygame.transform.scale(pygame.image.load('tasten/w.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_w.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
taste_a = pygame.transform.scale(pygame.image.load('tasten/a.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_a.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
taste_d = pygame.transform.scale(pygame.image.load('tasten/d.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_d.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
taste_hoch = pygame.transform.scale(pygame.image.load('tasten/hoch.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_hoch.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
taste_links = pygame.transform.rotate(taste_hoch, 90)
taste_rechts = pygame.transform.rotate(taste_hoch, 270)
backspace = pygame.transform.scale(pygame.image.load('tasten/backspace.png'), (int(gv.width / 18), int(gv.width / 34)))
backspace.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)


def build_level(self, index):
    self.selected_level = index
    self.blocks = []
    self.interactables = []
    self.wall_variations = []
    x = 0
    y = 0
    for row in all_levels[index]:
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
            elif char == "B":  # Halber Block
                blocks.append(Block(3, x, y + .5, height=.5))

            elif char == "R":  # Rechte Rampe
                blocks.append(Block(1, x, y))
            elif char == "L":  # Linke Rampe
                blocks.append(Block(2, x, y))

            elif char == "w":  # Wasser
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "e":  # Elektrizität
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "a":  # Säure
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))

            # Knöpfe und Türen
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

            elif char == "C":  # Position Current
                self.posCurrent = (x * gv.sc, y * gv.sc)
            elif char == "F":  # Position Flow
                self.posFlow = (x * gv.sc, y * gv.sc)

            elif char == " ":
                continue
            self.wall_variations.append(random.randint(0, len(all_wall_imgs) - 1))
            x += 1
        y += 1
        x = 0


def update(dt):
    # Knöpfe und Türen updaten
    for inter in interactables:
        if inter.__class__ == Button or inter.__class__ == Door:
            inter.update(dt)


def render(self, canvas):

    # Im ersten Level die Steuerung anzeigen
    if selected_level == 0:
        # Taste w
        canvas.blit(taste_w, (gv.width * 38 / 100, gv.height * 17 / 20))
        # Taste a
        canvas.blit(taste_a, (gv.width * 35 / 100, gv.height * 18 / 20))
        # Taste d
        canvas.blit(taste_d, (gv.width * 41 / 100, gv.height * 18 / 20))

        # Taste hoch
        canvas.blit(taste_hoch, (gv.width * 227 / 400, gv.height * 17 / 20))
        # Taste links
        canvas.blit(taste_links, (gv.width * 215 / 400, gv.height * 18 / 20))
        # Taste rechts
        canvas.blit(taste_rechts, (gv.width * 239 / 400, gv.height * 18 / 20))

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
        elif block.typ == 3:  # Halber Block
            canvas.blit(w_img_halb, (block.rect.x, block.rect.y))

        # Rampen in Form von Polygonen anhand des Rechtecks
        elif block.typ == 1:  # RampeR
            canvas.blit(ramp_r_img, (block.rect.x, block.rect.y))
        elif block.typ == 2:  # RampeL
            canvas.blit(ramp_l_img, (block.rect.x, block.rect.y))

    # Verlassen
    canvas.blit(text_surface, text_rect)
    # Backspace
    canvas.blit(backspace, (gv.width * 92 / 100, gv.height * 8 / 100))
