import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD_BIG = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 20)
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 30)

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD_BIG.render("CURRENT", (255, 255, 0))
text_surface2, rect2 = FONT_SD_BIG.render("FLOW", (0, 255, 255))
text_surface3, rect3 = FONT_SD.render("von", (255, 255, 255))
text_surface4, rect4 = FONT_SD.render("Valentin Kunisch", (255, 255, 255))
text_surface5, rect5 = FONT_SD.render("Ben Buller", (255, 255, 255))
text_surface6, rect6 = FONT_SD.render("Ann-Katrin Weihe", (255, 255, 255))
text_surface7, rect7 = FONT_SD.render("Lukas Sambale", (255, 255, 255))


def handleinput(event):
    if event.type == pygame.KEYDOWN:
        # Startbildschrim
        gv.active_stage = 0


def render(canvas):

    # CURRENT
    canvas.blit(text_surface1, (gv.width / 2 - rect1[2] + 30, gv.height * 2 / 10))
    # FLOW
    canvas.blit(text_surface2, (gv.width / 2 + 30, gv.height * 2 / 10 + 6))
    # gemacht von
    canvas.blit(text_surface3, (gv.width / 2 - rect3[2] / 2, gv.height * 7 / 20))
    # Valentin Kunisch
    canvas.blit(text_surface4, (gv.width / 2 - rect4[2] / 2, gv.height * 5 / 10))
    # Ben Buller
    canvas.blit(text_surface5, (gv.width / 2 - rect5[2] / 2, gv.height * 6 / 10))
    # Ann-Katrin Weihe
    canvas.blit(text_surface6, (gv.width / 2 - rect6[2] / 2, gv.height * 7 / 10))
    # Lukas Sambale
    canvas.blit(text_surface7, (gv.width / 2 - rect7[2] / 2, gv.height * 8 / 10))
