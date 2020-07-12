import pygame.freetype

import globalvalues as gv
import timer as t
import stage

# Das Freetype-Modul initialisieren
pygame.freetype.init()

level_nr = 1

# Objekt aus Schriftart erzeugen
FONT_SD = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 16)

# Sprites laden
enter = pygame.transform.scale(pygame.image.load('tasten/enter.png'), (int(gv.height / 15), int(gv.height / 15)))
leertaste = pygame.transform.scale(pygame.image.load('tasten/leertaste.png'), (int(gv.width / 10), int(gv.width / 40)))
hintergrund = pygame.transform.scale(pygame.image.load('wall_images/wall.png'), (int(gv.width / 3), int(gv.width / 3)))

# Schrift auf Surface zeichnen
text_surface1, rect1 = FONT_SD.render("Level " + str(level_nr) + "  ", (255, 255, 0))
text_surface2, rect2 = FONT_SD.render("geschafft!", (0, 255, 255))


def set_level(self, nummer):
    self.level_nr = nummer
    self.text_surface1, self.rect1 = FONT_SD.render("Level " + str(level_nr + 1) + "  ", (255, 255, 0))


def handleinput(event, stage, levelselect, current, flow):
    if event.type == pygame.KEYDOWN:

        # Bei Enter oder Leertaste zur nächsten Stage wechseln
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            if level_nr >= len(stage.all_levels) - 1:
                gv.active_stage = -4
            else:
                levelselect.selected = levelselect.selected_lev = stage.selected_level = level_nr + 1
                stage.build_level(stage, stage.selected_level)
                current.reset(stage.posCurrent[0], stage.posCurrent[1])
                flow.reset(stage.posFlow[0], stage.posFlow[1])
                gv.active_stage = 1


def render(canvas):
    # Hintergrund
    canvas.blit(hintergrund, (0, 0))
    canvas.blit(hintergrund, (gv.width / 3, 0))
    canvas.blit(hintergrund, (gv.width * 2 / 3, 0))
    canvas.blit(hintergrund, (0, gv.width / 3))
    canvas.blit(hintergrund, (gv.width / 3, gv.width / 3))
    canvas.blit(hintergrund, (gv.width * 2 / 3, gv.width / 3))

    stage.count = 2
    t.timer(t, stage.start_time, canvas)
    # Level x
    canvas.blit(text_surface1, (gv.width / 2 - ((rect1[2] + rect2[2]) / 2), gv.height / 2 - rect1[3] / 2))
    # geschafft!
    canvas.blit(text_surface2, (gv.width / 2 + ((rect1[2] + rect2[2]) / 2) - rect2[2], gv.height / 2 - rect2[3] / 2))
    # Leertaste
    canvas.blit(leertaste, (gv.width / 2 - ((leertaste.get_width() + enter.get_width() + gv.width / 50)/2), gv.height * 5 / 8 + gv.width / 96))
    # Enter
    canvas.blit(enter, (gv.width / 2 + ((leertaste.get_width() + enter.get_width() + gv.width / 50)/2) - enter.get_width() - gv.width / 100, gv.height * 5 / 8))

