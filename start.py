import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", 120)
text_surface, rect = FONT_SD.render("CURRENTFLOW", (255, 255, 0))


def handleinput(_event):
    if (_event.type == pygame.KEYDOWN and (_event.key == pygame.K_SPACE or pygame.K_RETURN))\
            or _event.type == pygame.MOUSEBUTTONDOWN:
        gv.active_stage = 1


def render(_window):
    tex = pygame.transform.scale(text_surface, (rect[2], rect[3]))
    _window.blit(tex, (gv.width / 2 - rect[2] / 2, gv.height / 2 - rect[3] / 2))
