import resize
import start
from players import *
import stage
import barriers as b
import interactables as i

pygame.init()

# Fenster
window = pygame.display.set_mode((gv.width, gv.height), flags=pygame.RESIZABLE)
pygame.display.set_caption("CurrentFlow")

# Hauptklassen
stage.build_level(stage, 0)
current = Player(False, 600 * gv.scale, 450 * gv.scale, (0, 255, 255))
flow = Player(True, 1000 * gv.scale, 450 * gv.scale, (255, 255, 0))

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
        elif event.type == pygame.VIDEORESIZE:
            resize.setdimensions(event.size[0], event.size[1])
            stage.build_level(stage, 0)

        # Eingabe
        if gv.active_stage == 0:
            start.handleinput(event)
        else:
            current.handleinput(event)
            flow.handleinput(event)

    # Update
    if gv.active_stage != 0:
        flow.update(dt, stage)
        current.update(dt, stage)

    # Render
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (33, 33, 33), (gv.L, gv.T, gv.width, gv.height))
    if gv.active_stage == 0:
        start.render(window)
    else:
        # i.Button.render(window)
        # i.Fluid.render(window)
        # i.Door.render(window)
        stage.render(stage, window)
        current.render(window)
        flow.render(window)

    # Canvas updaten
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
