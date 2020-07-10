import start
from players import *
import stage
import settings
import result_screen

pygame.init()

# Fenster
window = pygame.display.set_mode(settings.resolutions[3])
canvas = pygame.Surface((gv.width, gv.height))
pygame.display.set_caption("CurrentFlow")

# Hauptklassen
stage.build_level(stage, 1)
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
        else:
            current.handleinput(event)
            flow.handleinput(event)

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
