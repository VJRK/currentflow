import pygame.freetype

import globalvalues as gv
import stage
import timer as t

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD_80 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 13)
FONT_SD_50 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 20)
FONT_SD_SMALL = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD_80.render("Levelauswahl", (0, 255, 255))
rect1 = pygame.Rect(gv.width * 1 / 2 - rect1[2] / 2, gv.height * 2 / 13 - rect1[3] / 2, rect1[2], rect1[3])
text_surface2, rect2 = FONT_SD_SMALL.render("Fortsetzen", (0, 255, 255, 100))
rect2 = pygame.Rect(gv.width * 91 / 100 - rect2[2] / 2, gv.height * 1 / 18 - rect2[3] / 2, rect2[2], rect2[3])


# Level
text_surfaces_lev = []
rects_lev = []
i = 0
col = 1
for levelnum in range(len(stage.all_levels)):
    text_surfaces_lev.append(FONT_SD_50.render("Level " + str(levelnum + 1), (255, 255, 0))[0])
    rect = FONT_SD_50.render("Level " + str(levelnum + 1), (255, 255, 0))[1]
    if i == 6:
        rects_lev.append(pygame.Rect(gv.width * 3 / 6 - rect[2] / 2, gv.height / 7 + col * gv.width / 8 - rect[3] / 2,
                                     rect[2], rect[3]))
    elif i % 3 == 0:
        rects_lev.append(pygame.Rect(gv.width * 1 / 6 - rect[2] / 2, gv.height / 7 + col * gv.width / 8 - rect[3] / 2,
                                     rect[2], rect[3]))
    elif i % 3 == 1:
        rects_lev.append(pygame.Rect(gv.width * 3 / 6 - rect[2] / 2, gv.height / 7 + col * gv.width / 8 - rect[3] / 2,
                                     rect[2], rect[3]))
    elif i % 3 == 2:
        rects_lev.append(pygame.Rect(gv.width * 5 / 6 - rect[2] / 2, gv.height / 7 + col * gv.width / 8 - rect[3] / 2,
                                     rect[2], rect[3]))
        col += 1
    i += 1
del i, rect
all_rects = rects_lev

# Momentan gewähltes Feld
selected = 0
# Momentan gewähltes Level
selected_lev = 0

# Tasten
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 24), int(gv.width / 24)))
backspace = pygame.transform.scale(pygame.image.load('tasten/backspace.png'), (int(gv.width / 18), int(gv.width / 34)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))
taste_a = pygame.transform.scale(pygame.image.load('tasten/a.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_d = pygame.transform.scale(pygame.image.load('tasten/d.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_hoch = pygame.transform.scale(pygame.image.load('tasten/hoch.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_links = pygame.transform.rotate(taste_hoch, 90)
taste_rechts = pygame.transform.rotate(taste_hoch, 270)

hintergrund = pygame.transform.scale(pygame.image.load('wall_images/wall.png'), (int(gv.width / 3), int(gv.width / 3)))


def handleinput(self, event, current, flow):

    # Bei Tastendruck
    if event.type == pygame.KEYDOWN:

        # Links (LEFT oder A)
        if event.key in (pygame.K_LEFT, pygame.K_a):
            if self.selected > 0:
                self.selected -= 1

        # Rechts (RIGHT oder D)
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            if self.selected < len(all_rects) - 1:
                self.selected += 1

        # Hoch (UP oder W)
        if event.key in (pygame.K_UP, pygame.K_w):
            if self.selected == 6:
                self.selected -= 2
            elif self.selected > 2:
                self.selected -= 3

        # Runter (DOWN oder S)
        if event.key in (pygame.K_DOWN, pygame.K_s):
            if self.selected < 3:
                self.selected += 3
            else:
                self.selected = 6


        # Auswählen (Enter oder Space)
        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            # Gewähltes Level zuweisen
            stage.overlay = False
            self.selected_lev = stage.selected_level = self.selected
            stage.build_level(stage, stage.selected_level)
            current.reset(stage.posCurrent[0], stage.posCurrent[1])
            flow.reset(stage.posFlow[0], stage.posFlow[1])
            gv.active_stage = 1

        # bei BACK zurück zum spiel
        if event.key == pygame.K_BACKSPACE:
            gv.active_stage = 1
            t.total_pause += pygame.time.get_ticks() - t.start_pause


def render(canvas):
    # Hintergrund
    canvas.blit(hintergrund, (0, 0))
    canvas.blit(hintergrund, (gv.width / 3, 0))
    canvas.blit(hintergrund, (gv.width * 2 / 3, 0))
    canvas.blit(hintergrund, (0, gv.width / 3))
    canvas.blit(hintergrund, (gv.width / 3, gv.width / 3))
    canvas.blit(hintergrund, (gv.width * 2 / 3, gv.width / 3))

    # Fenster
    canvas.blit(text_surface1, rect1)

    # Level
    column = 1
    for j in range(len(stage.all_levels)):
        if j == 6:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 3 / 6 - rects_lev[j][2] / 2,
                         gv.height / 7 + column * gv.width / 8 - rects_lev[j][3] / 2))
        elif j % 3 == 0:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 1 / 6 - rects_lev[j][2] / 2,
                         gv.height / 7 + column * gv.width / 8 - rects_lev[j][3] / 2))
        elif j % 3 == 1:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 3 / 6 - rects_lev[j][2] / 2,
                         gv.height / 7 + column * gv.width / 8 - rects_lev[j][3] / 2))
        elif j % 3 == 2:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 5 / 6 - rects_lev[j][2] / 2,
                         gv.height / 7 + column * gv.width / 8 - rects_lev[j][3] / 2))
            column += 1

    # Fortsetzen
    canvas.blit(text_surface2, rect2)

    # Auswahl
    pygame.draw.rect(canvas, (255, 255, 255), (all_rects[selected][0] - 5, all_rects[selected][1] - 5,
                                               all_rects[selected][2] + 10, all_rects[selected][3] + 6), 2)
    # Gewähltes Level
    pygame.draw.line(canvas, (0, 255, 255),
                     (rects_lev[selected_lev][0] - 3,
                      rects_lev[selected_lev][1] + rects_lev[selected_lev][3] - 2),
                     (rects_lev[selected_lev][0] + rects_lev[selected_lev][2] + 3,
                      rects_lev[selected_lev][1] + rects_lev[selected_lev][3] - 2), 2)

    # Taste a
    canvas.blit(taste_a, (gv.width * 3 / 100, gv.height * 18 / 20))
    # Taste d
    canvas.blit(taste_d, (gv.width * 6 / 100, gv.height * 18 / 20))

    # Taste links
    canvas.blit(taste_links, (gv.width * 12 / 100, gv.height * 18 / 20))
    # Taste rechts
    canvas.blit(taste_rechts, (gv.width * 15 / 100, gv.height * 18 / 20))

    # Leertaste
    canvas.blit(leertaste, (gv.width * 44 / 50, gv.height * 90 / 100))
    # Enter
    canvas.blit(enter, (gv.width * 44 / 50 - gv.width / 20, gv.height * 88 / 100))
    # Backspace
    canvas.blit(backspace, (gv.width * 92 / 100, gv.height * 8 / 100))
