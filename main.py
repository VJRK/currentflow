import pygame

# Fenster
window = pygame.display.set_mode((1600, 900), flags=pygame.RESIZABLE)
pygame.display.set_caption("Currentflow")

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

    # Render
    window.fill((0, 0, 0))

    # Canvas updaten
    pygame.display.update()

    # Ende Game loop
    clock.tick(max_fps)
