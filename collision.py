from pygame import Rect


# Horizontale Kollisio
def horizontal_collisions(player, blocks):
    collisions = get_collisions(player, blocks)
    for collision in collisions:
        if collision.typ == 0:  # Wall
            # Rechtsbewegung
            if player.velX > 0:
                player.velX = 0
                player.posX = collision.rect.left - player.width / 2
            # Linksbewegung
            elif player.velX < 0:
                player.velX = 0
                player.posX = collision.rect.right + player.width / 2


# Vertikale Kollision
def vertical_collisions(player, blocks):
    collisions = get_collisions(player, blocks)
    for collision in collisions:

        # Aufwärtsbewegung
        if player.velY < 0:
            player.velY = 0
            player.posY = collision.rect.bottom + player.height / 2

        # Abwärtsbewegung
        elif player.velY > 0:

            # Rechte Rampe
            if collision.typ == 1:
                player.velY = 0

                # Wenn die rechte untere Ecke des Spielers auf der schiefen Ebene ist
                if player.posX + player.width / 2 < collision.rect.right:

                    # Höhe so bestimmen, dass die rechte untere Ecke des Spielers auf der Rampe ist
                    player.posY = collision.rect.bottom - player.height / 2 - \
                                  ((collision.rect.height / collision.rect.width)
                                   * (player.posX + player.width / 2 - collision.rect.left))
                else:
                    player.posY = collision.rect.top - player.height / 2

            # Linke Rampe
            elif collision.typ == 2:
                player.velY = 0

                # Wenn die linke untere Ecke des Spielers auf der schiefen Ebene ist
                if player.posX - player.width / 2 > collision.rect.left:

                    # Höhe so bestimmen, dass die linke untere Ecke des Spielers auf der Rampe ist
                    player.posY = collision.rect.bottom - player.height / 2 - collision.rect.height + \
                              ((collision.rect.height / collision.rect.width)
                               * (player.posX - player.width / 2 - collision.rect.left))
                else:
                    player.posY = collision.rect.top - player.height / 2

            else:  # Wall
                player.velY = 0
                player.posY = collision.rect.top - player.height / 2


# Findet alle Blöcke, die den Spieler berühren
def get_collisions(player, blocks):
    collisions = []
    pl_rect = Rect(player.posX - player.width / 2, player.posY - player.height / 2, player.width, player.height)
    for block in blocks:
        if pl_rect.colliderect(block.rect):
            block.color = (255, 0, 0)
            collisions.append(block)
        else:
            block.color = (255, 255, 255)
    return collisions
