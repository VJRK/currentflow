import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", 120)
# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD.render("CURRENT", (0, 255, 255))
text_surface2, rect2 = FONT_SD.render("FLOW", (255, 255, 0))


def handleinput(_event):
    # Bei Enter, Leertaste oder Mausklick die Szene wechseln
    if (_event.type == pygame.KEYDOWN and (_event.key == pygame.K_SPACE or pygame.K_RETURN))\
            or _event.type == pygame.MOUSEBUTTONDOWN:
        gv.active_stage = 1


def render(_window):
    # tex = pygame.transform.scale(text_surface, (rect[2], rect[3]))
    _window.blit(text_surface1, (gv.width / 2 - rect1[2], gv.height / 2 - rect1[3] / 2))
    _window.blit(text_surface2, (gv.width / 2, gv.height / 2 - rect2[3] / 2))
