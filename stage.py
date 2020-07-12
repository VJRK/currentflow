import random

import pygame.freetype

import timer as t
from block import *
from interactable import *
from level import *

# Das Freetype-Modul Initialisieren
pygame.freetype.init()

all_levels = [level1, level2, level3, level4, level5]
selected_level = 0
blocks = []
wall_variations = []
interactables = []
posCurrent = (0, 0)
posFlow = (0, 0)
overlay = False
count = 0

# "Verlassen"-Schriftzug in der oberen rechten Ecke
FONT_SD_SMALL = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)
text_surface1, rect1 = FONT_SD_SMALL.render("Verlassen", (0, 255, 255, 100))
text_rect1 = pygame.Rect(gv.width * 46 / 50 - rect1[2] / 2, gv.height * 1 / 18 - rect1[3] / 2, rect1[2], rect1[3])

# "Erneut versuchen"-Schriftzug auf dem Overlay
FONT_SD_BIG = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 20)
text_surface2, rect2 = FONT_SD_BIG.render("Erneut versuchen", (0, 255, 255))
text_rect2 = pygame.Rect(gv.width / 2 - rect2[2] / 2, gv.height / 2 - rect2[3] / 2, rect2[2], rect2[3])

# Sprites der Blöcke laden
w_img1 = pygame.transform.scale(pygame.image.load("wall_images/wand1.png"), (gv.sc, gv.sc))
w_img2 = pygame.transform.scale(pygame.image.load("wall_images/wand2.png"), (gv.sc, gv.sc))
w_img3 = pygame.transform.scale(pygame.image.load("wall_images/wand3.png"), (gv.sc, gv.sc))
w_img_halb = pygame.transform.scale(pygame.image.load("wall_images/wand_u.png"), (gv.sc, gv.sc))
ramp_r_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_r.png"), (gv.sc, gv.sc))
ramp_l_img = pygame.transform.scale(pygame.image.load("wall_images/rampe_l.png"), (gv.sc, gv.sc))
ziel_c = pygame.transform.scale(pygame.image.load("wall_images/ziel_c.png"), (gv.sc * 2, gv.sc * 4))
ziel_f = pygame.transform.scale(pygame.image.load("wall_images/ziel_f.png"), (gv.sc * 2, gv.sc * 4))
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

# Anleitung
font_sd_small = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 70)
text_surface3, rect3 = font_sd_small.render("Strom  und  Wasser  vertragen  sich  nicht  gut ...", (200, 200, 200))
text_surface4, rect4 = font_sd_small.render("Und  giftige  Schmieren  zersetzen  beide .", (200, 200, 200))
text_surface5, rect5 = font_sd_small.render("Current  +  Gelber  Knopf  =  Platform  hoch !", (200, 200, 200))
text_surface6, rect6 = font_sd_small.render("Flow  +  Blauer  Knopf  =  Tor  auf !", (200, 200, 200))


# Enter und Leertaste
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 24), int(gv.width / 24)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))


def build_level(self, index):
    self.count = 1
    self.start_time = pygame.time.get_ticks()
    t.total_pause = 0
    self.selected_level = index
    self.blocks = []
    self.interactables = []
    self.wall_variations = []
    x = 0
    y = 0
    for row in all_levels[index]:
        for char in row:

            if char == "W":
                blocks.append(Block(0, x, y))
            elif char == "B":  # Halber Block
                blocks.append(Block(3, x, y + .5, height=.5))

            elif char == "R":  # Rechte Rampe
                blocks.append(Block(1, x, y))
            elif char == "L":  # Linke Rampe
                blocks.append(Block(2, x, y))

            elif char == "u":  # Wasser
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "ù":  # Wasser + linke Rampe
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(2, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "ú":  # Wasser + rechte Rampe
                interactables.append(Fluid(0, x, y))
                blocks.append(Block(1, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))

            elif char == "e":  # Elektrizität
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            if char == "è":  # Elektrizität + linke Rampe
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(2, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "é":  # Elektrizität + rechte Rampe
                interactables.append(Fluid(1, x, y))
                blocks.append(Block(1, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))

            elif char == "a":  # Säure
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "à":  # Säure + linke Rampe
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(2, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))
            elif char == "á":  # Säure + rechte Rampe
                interactables.append(Fluid(2, x, y))
                blocks.append(Block(1, x, y))
                blocks.append(Block(3, x, y + .5, height=.5))

            # Knöpfe und Türen
            # Current
            elif char == "0":  # Knopf
                interactables.append(Button(1, x, y, activated_by=1))
            elif char == "1":  # Plattform hoch
                interactables.append(Door(1, x - 0.75, y + 0.5, height=0.5, width=2.5, target_height=-2))
            elif char == "2":  # Plattform runter
                interactables.append(Door(1, x - 0.75, y + 0.5, height=0.5, width=2.5, target_height=2.5))
            elif char == "3":  # Tür hoch
                interactables.append((Door(1, x + 0.25, y - 4, height=5, target_height=-5.5)))
            elif char == "4":  # Tür runter
                interactables.append(Door(1, x + 0.25, y - 4, height=5, target_height=5.5))
            # Flow
            elif char == "5":  # Knopf
                interactables.append(Button(2, x, y, activated_by=2))
            elif char == "6":  # Plattform hoch
                interactables.append(Door(2, x - 0.75, y + .5, height=0.5, width=2.75, target_height=-2))
            elif char == "7":  # Plattform runter
                interactables.append(Door(2, x - 0.75, y + 0.5, height=0.5, width=2.75, target_height=2.5))
            elif char == "8":  # Tür hoch
                interactables.append((Door(2, x + 0.25, y - 4, height=5, target_height=-5.5)))
            elif char == "9":  # Tür runter
                interactables.append(Door(2, x + 0.25, y - 4, height=5, target_height=5.5))

            # Spieler
            elif char == "C":  # Position Current
                self.posCurrent = (x * gv.sc, y * gv.sc)
            elif char == "F":  # Position Flow
                self.posFlow = (x * gv.sc, y * gv.sc)
            elif char == "c":  # Ziel Current
                blocks.append(Block(4, x - 0.5, y - 3, width=2, height=4))
            elif char == "f":  # Ziel Flow
                blocks.append(Block(5, x - 0.5, y - 3, width=2, height=4))

            elif char == " ":
                continue
            self.wall_variations.append(random.randint(0, len(all_wall_imgs) - 1))
            x += 1
        y += 1
        x = 0


def handleinput(self, event, current, flow):
    if overlay:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
            build_level(self, self.selected_level)
            current.reset(self.posCurrent[0], self.posCurrent[1])
            flow.reset(self.posFlow[0], self.posFlow[1])
            self.overlay = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            gv.active_stage = -3
    else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            gv.active_stage = -3
            t.start_pause = pygame.time.get_ticks()
        current.handleinput(event)
        flow.handleinput(event)


def update(dt, result_screen, current, flow):
    if current.in_goal and flow.in_goal:
        result_screen.set_level(result_screen, selected_level)
        gv.active_stage = -2

    # Knöpfe und Türen updaten
    for inter in interactables:
        if inter.__class__ == Button or inter.__class__ == Door:
            inter.update(dt)


def render(self, canvas):
    # Im ersten Level die Steuerung anzeigen
    if selected_level == 0:
        # Taste w
        canvas.blit(taste_w, (gv.width * 8 / 100, gv.height * 16 / 20))
        # Taste a
        canvas.blit(taste_a, (gv.width * 5 / 100, gv.height * 17 / 20))
        # Taste d
        canvas.blit(taste_d, (gv.width * 11 / 100, gv.height * 17 / 20))

        # Taste hoch
        canvas.blit(taste_hoch, (gv.width * 95 / 400, gv.height * 16 / 20))
        # Taste links
        canvas.blit(taste_links, (gv.width * 83 / 400, gv.height * 17 / 20))
        # Taste rechts
        canvas.blit(taste_rechts, (gv.width * 107 / 400, gv.height * 17 / 20))

        # Anleitung
        canvas.blit(text_surface3, (gv.width * 48 / 100 - rect3[2] / 2, gv.height * 79 / 100, rect3[2], rect3[3]))
        canvas.blit(text_surface4, (gv.width * 68 / 100 - rect4[2] / 2, gv.height * 51 / 100, rect4[2], rect4[3]))
        canvas.blit(text_surface5, (gv.width * 27 / 100 - rect5[2] / 2, gv.height * 56 / 100, rect5[2], rect5[3]))
        canvas.blit(text_surface6, (gv.width * 60 / 100 - rect6[2] / 2, gv.height * 23 / 100, rect6[2], rect6[3]))



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

        elif block.typ == 4:  # Ziel Current
            canvas.blit(ziel_c, (block.rect.x, block.rect.y))
        elif block.typ == 5:  # Ziel Flow
            canvas.blit(ziel_f, (block.rect.x, block.rect.y))

    # Verlassen
    canvas.blit(text_surface1, text_rect1)
    # Backspace
    canvas.blit(backspace, (gv.width * 92 / 100, gv.height * 8 / 100))

    if overlay:
        s = pygame.Surface((canvas.get_width(), canvas.get_height()))
        s.set_alpha(100)
        s.fill((0, 0, 0))
        canvas.blit(s, (0, 0))
        # Erneut versuchen
        canvas.blit(text_surface2, text_rect2)
        # Leertaste
        canvas.blit(leertaste, (gv.width / 2 - ((leertaste.get_width() + enter.get_width() + gv.width / 50)/2), gv.height * 5 / 8 + gv.width / 96))
        # Enter
        canvas.blit(enter, (gv.width / 2 + ((leertaste.get_width() + enter.get_width() + gv.width / 50)/2) - enter.get_width() - gv.width / 100, gv.height * 5 / 8))


    # Timer
    t.timer(t, self.start_time, canvas)
