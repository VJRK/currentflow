from interactable import *


# Horizontale Kollision
def horizontal_collisions(player, blocks):
    collisions = get_collisions(player, blocks)
    for collision in collisions:
        if collision.typ == 0 or collision.typ == 3:  # Wand oder Halber Block
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
        if collision.typ == 0 or collision.typ == 3:  # Wand oder Halber Block
            # Aufwärtsbewegung
            if player.velY < 0:
                player.velY = 0
                player.posY = collision.rect.bottom + player.height / 2
            # Abwärtsbewegung
            elif player.velY > 0:
                player.velY = 0
                player.posY = collision.rect.top - player.height / 2
                player.has_jump = True


# Rampenkollision
def ramp_collisions(player, blocks):
    collisions = get_collisions(player, blocks)
    for collision in collisions:
        if collision.typ == 1 or collision.typ == 2:  # RampeR oder RampeL

            # Aufwärtsbewegung
            if player.posY > collision.rect.bottom:
                player.velY = 0
                player.posY = collision.rect.bottom + player.height / 2

            # Rechte Rampe
            elif collision.typ == 1:

                # Wenn die rechte untere Ecke des Spielers auf der schiefen Ebene ist (X-Koordinate)
                if player.posX + player.width / 2 < collision.rect.right:

                    # Höhe der Rampe bei der unteren rechten Ecke des Spielers (X-Koordinate)
                    ramp_y = collision.rect.bottom - ((collision.rect.height / collision.rect.width)
                                                      * (player.posX + player.width / 2 - collision.rect.left))

                    # Wenn Spieler mit der Rampe kollidiert
                    if player.posY + player.height / 2 > ramp_y:
                        # Höhe so bestimmen, dass die rechte untere Ecke des Spielers auf der Rampe ist
                        player.posY = ramp_y - player.height / 2

                        # Spieler bewegen
                        player.velX -= player.velY / 2
                        player.velY = 0
                        player.has_jump = True
                else:
                    player.posY = collision.rect.top - player.height / 2

            # Linke Rampe
            elif collision.typ == 2:

                # Wenn die linke untere Ecke des Spielers auf der schiefen Ebene ist (X-Koordinate)
                if player.posX - player.width / 2 > collision.rect.left:

                    ramp_y = collision.rect.bottom - collision.rect.height + \
                             ((collision.rect.height / collision.rect.width)
                              * (player.posX - player.width / 2 - collision.rect.left))

                    # Wenn Spieler mit der Rampe kollidiert
                    if player.posY + player.height / 2 > ramp_y:

                        # Höhe so bestimmen, dass die linke untere Ecke des Spielers auf der Rampe ist
                        player.posY = ramp_y - player.height / 2

                        # Spieler bewegen
                        player.velX += player.velY / 2
                        player.velY = 0
                        player.has_jump = True
                else:
                    player.posY = collision.rect.top - player.height / 2


# Kollision mit Flüssigkeiten
def fluid_collisions(player, interactables):
    # Fluids von Interactables trennen
    fluids = []
    for inter in interactables:
        if inter.__class__ == Fluid:
            fluids.append(inter)
    # Kollisionen finden
    collisions = get_collisions(player, fluids)
    for collision in collisions:
        # Current und Wasser / Flow und Elektrizität / Säure
        if (not player.is_flow and collision.typ == 0) \
                or (player.is_flow and collision.typ == 1) \
                or collision.typ == 2:
            player.dead = True


# Kollision mit Knöpfen
def button_collisions(player, interactables):
    # Knöpfe und Türen ven den Interactables trennen
    buttons = []
    doors = []
    for inter in interactables:
        if inter.__class__ == Button:
            buttons.append(inter)
        elif inter.__class__ == Door:
            doors.append(inter)

    # Nicht gedrückte Knöpfe zurücksetzen
    collide_buttons = get_collisions(player, buttons)
    if not collide_buttons:
        for button in buttons:
            if player.is_flow == button.flow_pressed:
                button.pressed = False
                for door in doors:
                    if button.tag == door.tag:
                        door.open = False

    # Rechteck des Spielers
    pl_rect = Rect(player.posX - player.width / 2, player.posY - player.height / 2, player.width, player.height)

    # Knöpfe bei richtigem Kontakt aktivieren
    for button in buttons:
        if pl_rect.colliderect(button.rect) and (button.activated_by == 0
                                                 or (button.activated_by == 1 and not player.is_flow)
                                                 or (button.activated_by == 2 and player.is_flow)):
            button.pressed = True
            button.flow_pressed = player.is_flow
            for door in doors:
                if button.tag == door.tag:
                    door.open = True

    # Bei Kollisionen Spieler auf Knopf platzieren
    for collide_button in collide_buttons:
        player.posY = collide_button.rect.top - player.height / 2 + 2
        player.has_jump = True


# Horizontale Türkollision
def horizontal_door_collisions(player, interactables):
    # Türen von Interactables trennen
    doors = []
    for inter in interactables:
        if inter.__class__ == Door:
            doors.append(inter)

    # Kollisionen finden
    collide_doors = get_collisions(player, doors)
    for door in collide_doors:
        # Rechtsbewegung
        if player.velX > 0 and player.posX < door.rect.left:
            player.velX = 0
            player.posX = door.rect.left - player.width / 2
        # Linksbewegung
        elif player.velX < 0 and player.posX > door.rect.right:
            player.velX = 0
            player.posX = door.rect.right + player.width / 2


# Vertikale Türkollision
def vertical_door_collisions(player, interactables):
    # Türen von Interactables trennen
    doors = []
    for inter in interactables:
        if inter.__class__ == Door:
            doors.append(inter)

    collide_doors = get_collisions(player, doors)
    for door in collide_doors:
        # Aufwärtsbewegung
        if player.velY < 0:
            player.velY = 0
            player.posY = door.rect.bottom + player.height / 2
        # Abwärtsbewegung
        elif player.velY > 0:
            player.velY = 0
            player.posY = door.rect.top - player.height / 2
            player.has_jump = True


# Findet alle Objekte, die den Spieler berühren
def get_collisions(player, objects):
    collisions = []
    pl_rect = Rect(player.posX - player.width / 2, player.posY - player.height / 2, player.width, player.height)
    for obj in objects:
        if pl_rect.colliderect(obj.rect):
            collisions.append(obj)
    return collisions
