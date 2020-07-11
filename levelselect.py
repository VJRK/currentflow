import pygame.freetype
import globalvalues as gv
import stage

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD_80 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 24)
FONT_SD_50 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 30)

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD_80.render("Select  Level", (0, 255, 255))
rect1 = pygame.Rect(gv.width * 1 / 2 - rect1[2] / 2, gv.height * 2 / 13 - rect1[3] / 2, rect1[2], rect1[3])
text_surface2, rect2 = FONT_SD_80.render("Exit Menu", (0, 255, 255))
rect2 = pygame.Rect(gv.width * 1 / 2 - rect2[2] / 2, gv.height * 8 / 9 - rect2[3] / 2, rect2[2], rect2[3])

# Level
text_surfaces_lev = []
rects_lev = []
i = 0
col = 1
for levelnum in range(len(stage.all_levels)):
    text_surfaces_lev.append(FONT_SD_50.render("Level " + str(levelnum + 1), (255, 255, 0))[0])
    rect = FONT_SD_50.render("Level " + str(levelnum + 1), (255, 255, 0))[1]
    if i % 3 == 0:
        rects_lev.append(pygame.Rect(gv.width * 1 / 6 - rect[2] / 2, gv.height / 4 + col * gv.width / 20 - rect[3] / 2,
                                     rect[2], rect[3]))
    if i % 3 == 1:
        rects_lev.append(pygame.Rect(gv.width * 3 / 6 - rect[2] / 2, gv.height / 4 + col * gv.width / 20 - rect[3] / 2,
                                     rect[2], rect[3]))
    if i % 3 == 2:
        rects_lev.append(pygame.Rect(gv.width * 5 / 6 - rect[2] / 2, gv.height / 4 + col * gv.width / 20 - rect[3] / 2,
                                     rect[2], rect[3]))
        col += 1
    i += 1
del i, rect
all_rects = rects_lev + [rect2]

# Momentan gewähltes Feld
selected = len(all_rects) - 1
# Momentan gewähltes Level
selected_lev = 1

# Tasten
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 24), int(gv.width / 24)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))
taste_w = pygame.transform.scale(pygame.image.load('tasten/w.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_s = pygame.transform.scale(pygame.image.load('tasten/s.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_rechts = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load('tasten/hoch.png'), (int(gv.width / 40), int(gv.width / 40))), 90)
taste_links = pygame.transform.rotate(taste_rechts, 180)


def handleinput(self, event):

    # Bei Tastendruck
    if event.type == pygame.KEYDOWN:

        # Hoch (UP oder W, LEFT oder A)
        if event.key in (pygame.K_UP, pygame.K_w, pygame.K_LEFT, pygame.K_a):
            if self.selected > 0:
                self.selected -= 1

        # Runter (DOWN oder S, RIGHT oder D)
        if event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_RIGHT, pygame.K_d):
            if self.selected < len(all_rects) - 1:
                self.selected += 1

        # Auswählen (Enter oder Space)
        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            # Bei Exit zurück zum Level
            if self.selected == len(all_rects) - 1:
                gv.active_stage = 1
            # Gewähltes Level zuweisen
            else:
                self.selected_lev = self.selected
                stage.build_level(stage, selected_lev)
                gv.active_stage = 1

        # bei BACK zurück zum spiel
        if event.key == pygame.K_BACKSPACE:
            gv.active_stage = 1


def render(canvas):

    # Fenster
    canvas.blit(text_surface1, rect1)

    # Level
    column = 1
    for j in range(len(stage.all_levels)):
        if j % 3 == 0:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 1 / 6 - rects_lev[j][2] / 2,
                         gv.height / 4 + column * gv.width / 20 - rects_lev[j][3] / 2))
        if j % 3 == 1:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 3 / 6 - rects_lev[j][2] / 2,
                         gv.height / 4 + column * gv.width / 20 - rects_lev[j][3] / 2))
        if j % 3 == 2:
            canvas.blit(text_surfaces_lev[j],
                        (gv.width * 5 / 6 - rects_lev[j][2] / 2,
                         gv.height / 4 + column * gv.width / 20 - rects_lev[j][3] / 2))
            column += 1

    # Exit Menu
    canvas.blit(text_surface2, rect2)

    # Auswahl
    pygame.draw.rect(canvas, (255, 255, 255), (all_rects[selected][0] - 5, all_rects[selected][1] - 5,
                                               all_rects[selected][2] + 10, all_rects[selected][3] + 6), 2)
    # Gewähltes Level
    pygame.draw.line(canvas, (255, 0, 0),
                     (rects_lev[selected_lev][0] - 3,
                      rects_lev[selected_lev][1] + rects_lev[selected_lev][3] - 2),
                     (rects_lev[selected_lev][0] + rects_lev[selected_lev][2] + 3,
                      rects_lev[selected_lev][1] + rects_lev[selected_lev][3] - 2), 2)

    # Taste hoch
    canvas.blit(taste_rechts, (gv.width * 1 / 50, gv.height * 17 / 20))
    # Taste w
    canvas.blit(taste_w, (gv.width * 3 / 50, gv.height * 17 / 20))
    # Taste runter
    canvas.blit(taste_links, (gv.width * 1 / 50, gv.height * 18 / 20))
    # Taste s
    canvas.blit(taste_s, (gv.width * 3 / 50, gv.height * 18 / 20))
    # Leertaste
    canvas.blit(leertaste, (gv.width * 44 / 50, gv.height * 90 / 100))
    # Enter
    canvas.blit(enter, (gv.width * 44 / 50 - gv.width / 20, gv.height * 88 / 100))
