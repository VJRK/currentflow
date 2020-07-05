import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", 120)

# Zahnrad-Sprite laden
zahnrad = pygame.transform.scale(pygame.image.load('zahnrad.png'), (200, 200))

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD.render("CURRENT", (0, 255, 255))
text_surface2, rect2 = FONT_SD.render("FLOW", (255, 255, 0))


def handleinput(event):
    if event.type == pygame.KEYDOWN:

        # Bei S oder E zu den Einstellungen wechseln
        if event.key == pygame.K_s or pygame.K_e:
            gv.active_stage = -1

        # Bei Enter oder Leertaste zu Stage 1 wechseln
        elif event.key == pygame.K_SPACE or pygame.K_RETURN:
            gv.active_stage = 1


def render(canvas):
    canvas.blit(text_surface1, (800 - rect1[2], 450 - rect1[3] / 2))
    canvas.blit(text_surface2, (800, 450 - rect2[3] / 2))
    canvas.blit(zahnrad, (1400, 700))
