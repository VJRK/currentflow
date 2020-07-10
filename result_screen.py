import pygame.freetype
import globalvalues as gv

# Das Freetype-Modul initialisieren
pygame.freetype.init()

level_nr = 1

# Objekt aus Schriftart erzeugen
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 20)

# Sprites laden
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.width / 30), int(gv.width / 21)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 9.6), int(gv.width / 48)))

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD.render("Level " + str(level_nr) + " ", (255, 255, 0))
text_surface2, rect2 = FONT_SD.render("geschafft!", (0, 255, 255))


def handleinput(event, stage):
    if event.type == pygame.KEYDOWN:

        # Bei Enter oder Leertaste zur nächsten Stage wechseln
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            gv.active_stage = level_nr + 1
            stage.build_level(stage, gv.active_stage - 1)


def render(canvas):
    # Level x
    canvas.blit(text_surface1, (gv.width / 2 - rect1[2], gv.height / 2 - rect1[3] / 2))
    # geschafft!
    canvas.blit(text_surface2, (gv.width / 2, gv.height / 2 - rect2[3] / 2))
    # Leertaste
    canvas.blit(leertaste, (gv.width / 2 - leertaste.get_width() - gv.width / 76, gv.height * 3 / 5 + 35))
    # Enter
    canvas.blit(enter, (gv.width / 2 + gv.width / 76, gv.height * 3 / 5))

