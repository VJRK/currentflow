import copy

import pygame.freetype

import globalvalues as gv
import stage

passed_time = 0
start_pause = 0
total_pause = 0

# Das Freetype-Modul initialisieren
pygame.freetype.init()


def timer(self, start, window):
    if stage.count == 1:
        time = int((pygame.time.get_ticks() - start - total_pause) / 1000)
        self.passed_time = copy.deepcopy(time)

    minutes, rem = divmod(passed_time, 60)
    seconds, deciseconds = divmod(rem, 10)

    font_sd_small = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)
    font_sd_middle = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 30)
    font_sd_big = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 22)

    if stage.count == 1:
        text_surfacetime, recttime = font_sd_small.render(str(int(minutes)) + " : " + str(int(seconds)) + " " +
                                                      str(int(deciseconds)), (255, 255, 255, 100))
        text_recttime = pygame.Rect(gv.width * 1 / 2 - recttime[2] / 2, gv.height * 1 / 20, recttime[2], recttime[3])

        window.blit(text_surfacetime, text_recttime)
    else:
        text_surface1, rect1 = font_sd_big.render("Gebrauchte Zeit", (255, 255, 255))
        text_surfacetime, recttime = font_sd_middle.render(str(int(minutes)) + " : " + str(int(seconds)) + " " +
                                                      str(int(deciseconds)), (255, 255, 255))
        text_recttime = pygame.Rect(gv.width * 1 / 2 - recttime[2] / 2, gv.height * 6 / 10, recttime[2], recttime[3])
        text_rect1 = pygame.Rect(gv.width * 1 / 2 - rect1[2] / 2, gv.height * 5 / 10, rect1[2], rect1[3])

        window.blit(text_surfacetime, text_recttime)
        window.blit(text_surface1, text_rect1)

