import pygame
import globalvalues as gv
import resize
import current as cu
import flow as fl
import level
import barriers
import start

# Fenster
window = pygame.display.set_mode((gv.width, gv.height), flags=pygame.RESIZABLE)
pygame.display.set_caption("Currentflow")

# Game loop
clock = pygame.time.Clock()
max_fps = 60
dt = clock.tick(max_fps)
running = True

level.compile_level(level.level2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            resize.setdimensions(event.size[0], event.size[1])

        # Eingabe
        if gv.active_stage == 0:
            start.handleinput(event)
        else:
            cu.handleinput(cu, event)
            fl.handleinput(fl, event)

    # Update
    if gv.active_stage != 0:
        cu.update(cu, dt)
        fl.update(fl, dt)

    # Render
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (33, 33, 33), (gv.L, gv.T, gv.width, gv.height))
    if gv.active_stage == 0:
        start.render(window)
    else:
        cu.render(window)
        fl.render(window)
        barriers.Barrier.render_barriers(window)

    # Canvas updaten
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
