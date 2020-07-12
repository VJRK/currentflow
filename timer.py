import pygame
import globalvalues as gv
import stage
import copy
passed_time = 0


def timer(self, start):
    if stage.count == 1:
        time = int((pygame.time.get_ticks() - start) / 1000)
        self.passed_time = copy.deepcopy(time)

    minutes, rem = divmod(passed_time, 60)
    seconds, deciseconds = divmod(rem, 10)
    return minutes, seconds, deciseconds


def render(minutes, seconds, deciseconds, window):
    if stage.count == 1:
        FONT_SD_SMALL = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)
        text_surfacetime, recttime = FONT_SD_SMALL.render(str(int(minutes)) + " . " + str(int(seconds)) + " " + str(int(deciseconds)), (255, 255, 255, 100))
        text_recttime = pygame.Rect(gv.width * 1 / 2, gv.height * 1 / 20, recttime[2], recttime[3])
        window.blit(text_surfacetime, text_recttime)
    elif stage.count == 2:
        FONT_SD_SMALL = pygame.freetype.Font("sheeping_dogs.ttf", gv.width / 48)
        text_surfacetime, recttime = FONT_SD_SMALL.render(str(int(minutes)) + " . " + str(int(seconds)) + " " + str(int(deciseconds)), (255, 255, 255))
        text_recttime = pygame.Rect(gv.width * 1 / 2, gv.height * 11 / 20, recttime[2], recttime[3])
        window.blit(text_surfacetime, text_recttime)




