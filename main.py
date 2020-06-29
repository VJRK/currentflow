import pygame
import globalvalues as gv
import current as cu
from level import *
from barriers import *
import flow as fl
import start

# Fenster
window = pygame.display.set_mode((gv.width, gv.height))
pygame.display.set_caption("Currentflow")

# Game loop
clock = pygame.time.Clock()
max_fps = 60
dt = clock.tick(max_fps)
running = True

compile_level(level2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

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
    if gv.active_stage == 0:
        start.render(window)
    else:
        cu.render(window)
        Barrier.render_barriers(window)
        fl.render(window)

    # Canvas updaten
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
