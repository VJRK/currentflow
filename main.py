import resize
import start
from players import *
import stage
import settings
import barriers as b
import interactables as i

pygame.init()

# Fenster
window = pygame.display.set_mode((gv.width, gv.height))
canvas = pygame.Surface((1600, 900))
pygame.display.set_caption("CurrentFlow")

# Hauptklassen
stage.build_level(stage, 0)
current = Player(False, 600, 450, (0, 255, 255))
flow = Player(True, 1000, 450, (255, 255, 0))

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
        else:
            current.handleinput(event)
            flow.handleinput(event)

    # Update
    print(gv.active_stage)
    if gv.active_stage != 0:
        flow.update(dt, stage)
        current.update(dt, stage)

    # Render
    canvas.fill((33, 33, 33))
    if gv.active_stage == 0:
        start.render(canvas)
    elif gv.active_stage == -1:
        settings.render(canvas)
    else:
        # i.Button.render(window)
        # i.Fluid.render(window)
        # i.Door.render(window)
        stage.render(stage, canvas)
        current.render(canvas)
        flow.render(canvas)

    # Canvas auf Fenster skalieren und zeichnen
    window.fill((0, 0, 0))
    window.blit(pygame.transform.scale(canvas, settings.resolutions[settings.selected_res]), (0, 0))
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
