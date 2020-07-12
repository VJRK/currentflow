import pygame.freetype
import globalvalues as gv
import stage
import copy
passed_time = 0

# Das Freetype-Modul initialisieren
pygame.freetype.init()


def timer(self, start, window):
    if stage.count == 1:
        time = int((pygame.time.get_ticks() - start) / 1000)
        self.passed_time = copy.deepcopy(time)

    minutes, rem = divmod(passed_time, 60)
    seconds, deciseconds = divmod(rem, 10)

    font_sd_small = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)

    if stage.count == 1:
        alpha = 100
    else:
        alpha = 255

    text_surfacetime, recttime = font_sd_small.render(str(int(minutes)) + " . " + str(int(seconds)) + " " +
                                                      str(int(deciseconds)), (255, 255, 255, alpha))
    if stage.count == 1:
        text_recttime = pygame.Rect(gv.width * 1 / 2 - recttime[2] / 2, gv.height * 1 / 20, recttime[2], recttime[3])
    else:
        text_recttime = pygame.Rect(gv.width * 1 / 2 - recttime[2] / 2, gv.height * 7 / 10, recttime[2], recttime[3])

    window.blit(text_surfacetime, text_recttime)
