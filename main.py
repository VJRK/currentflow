import start
import resize
from players import *
import stage
import settings
import result_screen
import levelselect

pygame.init()

# Fenster (wählt automatisch passende Auflösung aus (siehe resize.py))
monitor_res = (pygame.display.Info().current_w, pygame.display.Info().current_h)
settings.selected_res = resize.get_resolution_index(monitor_res[0], monitor_res[1])
window = pygame.display.set_mode(settings.resolutions[settings.selected_res])
canvas = pygame.Surface((gv.width, gv.height))
pygame.display.set_caption("CurrentFlow")

# Hauptklassen
stage.build_level(stage, levelselect.selected_lev)
current = Player(False, stage.posCurrent[0], stage.posCurrent[1], (255, 255, 0))
flow = Player(True, stage.posFlow[0], stage.posFlow[1], (0, 255, 255))

# Game loop
clock = pygame.time.Clock()
max_fps = 60
dt = clock.tick(max_fps)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # Eingabe
        if gv.active_stage == 0:
            start.handleinput(event)
        elif gv.active_stage == -1:
            settings.handleinput(settings, event, window)
        elif gv.active_stage == -2:
            result_screen.handleinput(event, stage)
        elif gv.active_stage == -3:
            levelselect.handleinput(levelselect, event, current, flow)
        else:
            current.handleinput(event)
            flow.handleinput(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                gv.active_stage = -3

    # Update
    if gv.active_stage != 0:
        flow.update(dt, stage)
        current.update(dt, stage)
        stage.update(dt)

    # Render
    canvas.fill((33, 33, 33))
    if gv.active_stage == 0:
        start.render(canvas)
    elif gv.active_stage == -1:
        settings.render(canvas)
    elif gv.active_stage == -2:
        result_screen.render(canvas)
    elif gv.active_stage == -3:
        levelselect.render(canvas)
    else:
        stage.render(stage, canvas)
        current.render(canvas)
        flow.render(canvas)

    # Canvas auf Fenster skalieren und zeichnen
    window.fill((0, 0, 0))
    window.blit(pygame.transform.scale(canvas, settings.resolutions[settings.selected_res]), (0, 0))
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
