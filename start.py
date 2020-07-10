import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

# Objekt aus Schriftart erzeugen
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 16)

# Sprites laden
zahnrad = pygame.transform.scale(pygame.image.load('zahnrad.png'), (int(gv.width / 9.6), int(gv.width / 9.6)))
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 24), int(gv.width / 24)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))
taste_e = pygame.transform.scale(pygame.image.load('tasten/e.png'), (int(gv.width / 40), int(gv.width / 40)))
hintergrund = pygame.transform.scale(pygame.image.load('wall_images/wall.png'), (int(gv.width / 4), int(gv.width / 4)))

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD.render("CURRENT", (255, 255, 0))
text_surface2, rect2 = FONT_SD.render("FLOW", (0, 255, 255))


def handleinput(event):
    if event.type == pygame.KEYDOWN:

        # Bei E zu den Einstellungen wechseln
        if event.key == pygame.K_e:
            gv.active_stage = -1

        # Bei Enter oder Leertaste zu Stage 1 wechseln
        elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            gv.active_stage = 1


def render(canvas):
    # Hintergrund
    canvas.blit(hintergrund, (0, 0))

    # CURRENT
    canvas.blit(text_surface1, (gv.width / 2 - rect1[2], gv.height / 2 - rect1[3] / 2))
    # FLOW
    canvas.blit(text_surface2, (gv.width / 2, gv.height / 2 - rect2[3] / 2))
    # Leertaste
    canvas.blit(leertaste, (gv.width / 2 - leertaste.get_width() - gv.width / 76, gv.height * 3 / 5 + gv.width / 96))
    # Enter
    canvas.blit(enter, (gv.width / 2 + gv.width / 76, gv.height * 3 / 5))

    # Zahnrad
    canvas.blit(zahnrad, (gv.width * 7 / 8, gv.height * 7 / 9))
    # Taste e
    canvas.blit(taste_e, (gv.width * 7 / 8 + zahnrad.get_width() / 2 - taste_e.get_width() / 2, gv.height * 7 / 10))
