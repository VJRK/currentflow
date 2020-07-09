import globalvalues as gv
from pygame import Rect


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


def check_horizontal_collisions(player, blocks):
    collide_walls = get_collisions(player, blocks)
    for collide_wall in collide_walls:
        if player.velY > 0:
            player.posX = collide_wall.rect.left - player.width / 2
            player.velY = 0
            player.collision_types['right'] = True
        elif player.velY < 0:
            player.posX = collide_wall.rect.right + player.width / 2
            player.velY = 0
            player.collision_types['left'] = True


def check_vertical_collisions(player, blocks):
    collide_walls = get_collisions(player, blocks)
    for collide_wall in collide_walls:
        if player.velY > 0:
            player.posY = collide_wall.rect.top - player.height / 2

            if abs(player.velY) < gv.base_run_speed and player.velY != 0:
                player.velY = 0

            player.velY = 0
            player.collision_types['bottom'] = True
        elif player.velY < 0:
            player.posY = collide_wall.rect.bottom + player.height / 2
            player.velY *= -0.8
            player.collision_types['top'] = True


def check_ramp_collisions(entity, ramps):
    collide_ramps = get_collisions(entity, ramps)
    for collide_ramp in collide_ramps:
        rel_x = entity.rect.x - collide_ramp.rect.x
        if collide_ramp.typ == "RampR":
            pos_height = rel_x + entity.rect.width
        if collide_ramp.typ == "RampL":
            pos_height = gv.scale - rel_x
        pos_height = min(pos_height, gv.scale)
        pos_height = max(pos_height, 0)
        target_y = collide_ramp.rect.y + gv.scale - pos_height
        if collide_ramp.typ == "RampR" and rel_x > entity.rect.width and entity.velY < 0:
            entity.rect.left = collide_ramp.rect.right
            entity.velY = 0
            entity.collision_types['left'] = True
        elif collide_ramp.typ == "RampL" and rel_x < 0 < entity.velY:
            entity.rect.right = collide_ramp.rect.left
            entity.velY = 0
            entity.collision_types['right'] = True
        elif entity.rect.bottom > collide_ramp.rect.bottom and entity.velY <= 0:
            entity.rect.top = collide_ramp.rect.bottom
            entity.velY = 0
            entity.collision_types['top'] = True
        elif entity.rect.bottom > target_y:
            entity.rect.bottom = target_y
            entity.velY = 0
            if entity.velY == 0 and collide_ramp.typ == "RampR" and rel_x < gv.scale:
                entity.velY = -gv.slide_speed
                entity.velY = -gv.slide_speed
            if entity.velY == 0 and collide_ramp.typ == "RampL":
                entity.velY = gv.slide_speed
                entity.velY = -gv.slide_speed
        entity.collision_types['bottom'] = True


def check_fluid_collisions(entity, fluids):
    collide_fluids = get_collisions(entity.rect, fluids)
    for collide_fluid in collide_fluids:
        if entity.name == "current" and collide_fluid.typ == "water":
            entity.dead = True
            entity.color = (100, 100, 100)
        elif entity.name == "flow" and collide_fluid.typ == "electricity":
            entity.dead = True
            entity.color = (100, 100, 100)
        elif collide_fluid.typ == "acid":
            entity.dead = True
            entity.color = (100, 100, 100)


def check_button_collision(entity, buttons, doors):
    collide_buttons = get_collisions(entity.rect, buttons)
    if not collide_buttons:
        for button in buttons:
            if entity.name == button.who_pressed:
                button.pressed = False
                for door in doors:
                    if button.tag == door.tag:
                        door.open = False

    for collide_button in collide_buttons:
        for door in doors:
            if collide_button.tag == door.tag:
                door.open = True

        collide_button.pressed = True
        collide_button.who_pressed = entity.name
        collide_button.press_speed = .1

        rel_x = entity.rect.x - collide_button.rect.x
        if rel_x >= collide_button.rect.width-collide_button.rect.height:
            pos_height = collide_button.rect.width - rel_x
        elif rel_x <= -entity.rect.width+collide_button.rect.height:
            pos_height = rel_x + entity.rect.width
        else:
            pos_height = collide_button.rect.height
        target_y = collide_button.rect.top + collide_button.rect.height - pos_height

        if entity.rect.bottom > target_y:
            entity.rect.bottom = target_y
            entity.velY = 0
        entity.collision_types['bottom'] = True


def check_door_collisions(entity, doors):
    collide_doors = get_collisions(entity, doors)
    for collide_door in collide_doors:
        if collide_door.velY == 0:
            if entity.velY > 0:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = 0
                entity.collision_types['bottom'] = True
            elif entity.velY < 0:
                entity.rect.top = collide_door.rect.bottom
                entity.velY = 0
                entity.collision_types['top'] = True
        else:
            if collide_door.velY < 0 and entity.rect.top < collide_door.rect.top:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = -.1
                entity.collision_types['bottom'] = True
            elif collide_door.velY > 0 and entity.rect.top < collide_door.rect.top:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = .1
                entity.collision_types['bottom'] = True
            if collide_door.rect.top < entity.rect.bottom - (entity.rect.height/2):
                entity.dead = True
                entity.color = (100, 100, 100)
            if collide_door.rect.bottom < entity.rect.top - (entity.rect.height/2):
                entity.dead = True
                entity.color = (100, 100, 100)


def update_collisions(player, blocks):
    check_vertical_collisions(player, blocks)
    check_horizontal_collisions(player, blocks)
