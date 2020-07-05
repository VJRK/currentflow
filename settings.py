import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD_80 = pygame.freetype.Font("sheeping_dogs.ttf", 80)
FONT_SD_50 = pygame.freetype.Font("sheeping_dogs.ttf", 50)

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD_80.render("Fenster", (0, 255, 255))
rect1 = pygame.Rect(600 - rect1[2] / 2, 200 - rect1[3] / 2, rect1[2], rect1[3])
text_surface2, rect2 = FONT_SD_80.render("Fertig", (0, 255, 255))
rect2 = pygame.Rect(1000 - rect2[2] / 2, 700 - rect2[3] / 2, rect2[2], rect2[3])

resolutions = [(1920, 1080), (1760, 990), (1600, 900), (800, 450)]
text_surfaces_res = []
rects_res = []
i = 0
for resolution in resolutions:
    text_surfaces_res.append(FONT_SD_50.render(str(resolution[0]) + " x " + str(resolution[1]), (255, 255, 0))[0])
    rect = FONT_SD_50.render(str(resolution[0]) + " x " + str(resolution[1]), (255, 255, 0))[1]
    rects_res.append(pygame.Rect(600 - rect[2] / 2, 300 + i * 100 - rect[3] / 2, rect[2], rect[3]))
    i += 1
del i, rect
all_rects = rects_res + [rect2]

# Momentan gewähltes Feld
selected = 2
# Momentan gewählte Auflösung
selected_res = 2


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
                self.selected_res = self.selected
                window = pygame.display.set_mode((resolutions[selected_res][0], resolutions[selected_res][1]))


def render(canvas):
    canvas.blit(text_surface1, rect1)
    for j in range(len(resolutions)):
        canvas.blit(text_surfaces_res[j], (600 - rects_res[j][2] / 2, 300 + j * 100 - rects_res[j][3] / 2))
    canvas.blit(text_surface2, rect2)
    pygame.draw.rect(canvas, (255, 255, 255), all_rects[selected], 6)
    pygame.draw.rect(canvas, (255, 0, 0), rects_res[selected_res], 3)
