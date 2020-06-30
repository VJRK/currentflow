import pygame
import globalvalues as gv
import resize
import level
import barriers as b
import interactables as i
import start
from players import *

# Fenster
pygame.init()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
resize.setdimensions(width, height)
window = pygame.display.set_mode((64 * gv.scale, 36 * gv.scale), flags=pygame.RESIZABLE)
pygame.display.set_caption("CurrentFlow")

# Game loop
clock = pygame.time.Clock()
max_fps = 60
dt = clock.tick(max_fps)
running = True

flow, current = level.assemble_level(0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            resize.setdimensions(event.size[0], event.size[1])
            window = pygame.display.set_mode((64 * gv.scale, 36 * gv.scale), flags=pygame.RESIZABLE)
            flow, current = level.assemble_level(0)

        # Eingabe
        if gv.active_stage == 0:
            start.handleinput(event)
        else:
            current.handleinput(event)
            flow.handleinput(event)

    # Update
    if gv.active_stage != 0:
        flow.update(dt)
        current.update(dt)
        for button in Button.instances:
            Button.update(button, dt)
        for door in Door.instances:
            Door.update(door, dt)

    # Render
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (33, 33, 33), (0, 0, 64 * gv.scale, 36 * gv.scale))
    if gv.active_stage == 0:
        start.render(window)
    else:
        i.Button.render(window)
        current.render(window)
        flow.render(window)
        i.Fluid.render(window)
        i.Door.render(window)
        b.Barrier.render(window)

    # Canvas updaten
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
