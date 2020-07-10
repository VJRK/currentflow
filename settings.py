import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD_80 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 24)
FONT_SD_50 = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 40)

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD_80.render("Fenster", (0, 255, 255))
rect1 = pygame.Rect(gv.width / 3 - rect1[2] / 2, gv.height * 2 / 9 - rect1[3] / 2, rect1[2], rect1[3])
text_surface2, rect2 = FONT_SD_80.render("Fertig", (0, 255, 255))
rect2 = pygame.Rect(gv.width * 2 / 3 - rect2[2] / 2, gv.height * 7 / 9 - rect2[3] / 2, rect2[2], rect2[3])

# Auflösungen
resolutions = [(3840, 2160), (3200, 1800), (2560, 1440), (1920, 1080), (1600, 900), (1280, 720), (640, 360)]
text_surfaces_res = []
rects_res = []
i = 0
for resolution in resolutions:
    text_surfaces_res.append(FONT_SD_50.render(str(resolution[0]) + " x " + str(resolution[1]), (255, 255, 0))[0])
    rect = FONT_SD_50.render(str(resolution[0]) + " x " + str(resolution[1]), (255, 255, 0))[1]
    rects_res.append(pygame.Rect(gv.width / 3 - rect[2] / 2, gv.height / 3 + i * gv.width / 25 - rect[3] / 2,
                                 rect[2], rect[3]))
    i += 1
del i, rect
all_rects = rects_res + [rect2]

# Momentan gewähltes Feld
selected = len(all_rects) - 1
# Momentan gewählte Auflösung
selected_res = 5

# Tasten
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 24), int(gv.width / 24)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))
taste_w = pygame.transform.scale(pygame.image.load('tasten/w.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_s = pygame.transform.scale(pygame.image.load('tasten/s.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_hoch = pygame.transform.scale(pygame.image.load('tasten/hoch.png'), (int(gv.width / 40), int(gv.width / 40)))
taste_runter = pygame.transform.rotate(taste_hoch, 180)


def handleinput(self, event, window):

    # Bei Tastendruck
    if event.type == pygame.KEYDOWN:
        # Hoch (UP oder W)
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            if self.selected > 0:
                self.selected -= 1
        # Runter (DOWN oder S)
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if self.selected < len(all_rects) - 1:
                self.selected += 1
        # Auswählen (Enter oder Space)
        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
            # Bei Fertig zurück zum Startbildschirm
            if self.selected == len(all_rects) - 1:
                gv.active_stage = 0
            # Gewählte Auflösung zuweisen
            else:
                self.selected_lev = self.selected
                window = pygame.display.set_mode((resolutions[selected_res][0], resolutions[selected_res][1]))


def render(canvas):
    # Fenster
    canvas.blit(text_surface1, rect1)
    # Auflösungen
    for j in range(len(resolutions)):
        canvas.blit(text_surfaces_res[j],
                    (gv.width / 3 - rects_res[j][2] / 2, gv.height / 3 + j * gv.width / 25 - rects_res[j][3] / 2))
    # Fertig
    canvas.blit(text_surface2, rect2)
    # Auswahl
    pygame.draw.rect(canvas, (255, 255, 255), (all_rects[selected][0] - 5, all_rects[selected][1] - 5,
                                               all_rects[selected][2] + 10, all_rects[selected][3] + 6), 2)
    # Gewählte Auflösung
    pygame.draw.line(canvas, (255, 0, 0),
                     (rects_res[selected_res][0] - 3,
                      rects_res[selected_res][1] + rects_res[selected_res][3] - 2),
                     (rects_res[selected_res][0] + rects_res[selected_res][2] + 3,
                      rects_res[selected_res][1] + rects_res[selected_res][3] - 2), 2)

    # Taste hoch
    canvas.blit(taste_hoch, (gv.width * 3 / 25, gv.height * 2 / 7))
    # Taste w
    canvas.blit(taste_w, (gv.width * 4 / 25, gv.height * 2 / 7))
    # Taste runter
    canvas.blit(taste_runter, (gv.width * 3 / 25, gv.height * 3 / 4))
    # Taste s
    canvas.blit(taste_s, (gv.width * 4 / 25, gv.height * 3 / 4))
    # Leertaste
    canvas.blit(leertaste, (gv.width * 2 / 3, gv.height / 2))
    # Enter
    canvas.blit(enter, (gv.width * 2 / 3 - gv.width / 20, gv.height / 2))
