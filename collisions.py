import globalvalues as gv

def test_collisions(entity, blocks):
    collisions = []
    for block in blocks:
        if entity.colliderect(block.rect):
            collisions.append(block)
    return collisions


def check_vertical_collisions(entity, blocks):
    collide_walls = test_collisions(entity.rect, blocks)
    for collide_wall in collide_walls:
        if entity.velY > 0:
            entity.rect.bottom = collide_wall.rect.top
            if abs(entity.velX) < gv.base_run_speed and entity.velX != 0:
                entity.velX = 0
            entity.velY = 0
            entity.collision_types['bottom'] = True
        elif entity.velY < 0:
            entity.rect.top = collide_wall.rect.bottom
            entity.velY = 0
            entity.collision_types['top'] = True


def check_ramp_collisions(entity, ramps):
    collide_ramps = test_collisions(entity.rect, ramps)
    for collide_ramp in collide_ramps:
        rel_x = entity.rect.x - collide_ramp.rect.x
        if collide_ramp.typ == "RampR":
            pos_height = rel_x + entity.rect.width
        if collide_ramp.typ == "RampL":
            pos_height = gv.scale - rel_x
        pos_height = min(pos_height, gv.scale)
        pos_height = max(pos_height, 0)
        target_y = collide_ramp.rect.y + gv.scale - pos_height
        if collide_ramp.typ == "RampR" and rel_x > entity.rect.width and entity.velX < 0:
            entity.rect.left = collide_ramp.rect.right
            entity.velX = 0
            entity.collision_types['left'] = True
        elif collide_ramp.typ == "RampL" and rel_x < 0 and entity.velX > 0:
            entity.rect.right = collide_ramp.rect.left
            entity.velX = 0
            entity.collision_types['right'] = True
        elif entity.rect.bottom > collide_ramp.rect.bottom and entity.velY <= 0:
            entity.rect.top = collide_ramp.rect.bottom
            entity.velY = 0
            entity.collision_types['top'] = True
        elif entity.rect.bottom > target_y:
            entity.rect.bottom = target_y
            entity.velY = 0
            if entity.velX == 0 and collide_ramp.typ == "RampR" and rel_x < gv.scale:
                entity.velX = -gv.slide_speed
                entity.velY = -gv.slide_speed
            if entity.velX == 0 and collide_ramp.typ == "RampL":
                entity.velX = gv.slide_speed
                entity.velY = -gv.slide_speed
        entity.collision_types['bottom'] = True


def check_horizontal_collisions(entity, blocks):
    collide_walls = test_collisions(entity.rect, blocks)
    for collide_wall in collide_walls:
        if entity.velX > 0:
            entity.rect.right = collide_wall.rect.left
            entity.velX = 0
            entity.collision_types['right'] = True
        elif entity.velX < 0:
            entity.rect.left = collide_wall.rect.right
            entity.velX = 0
            entity.collision_types['left'] = True


def check_fluid_collisions(entity, fluids):
    collide_fluids = test_collisions(entity.rect, fluids)
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
    collide_buttons = test_collisions(entity.rect, buttons)
    if collide_buttons == []:
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
    collide_doors = test_collisions(entity.rect, doors)
    for collide_door in collide_doors:
        if collide_door.velX == 0:
            if entity.velY > 0:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = 0
                entity.collision_types['bottom'] = True
            elif entity.velY < 0:
                entity.rect.top = collide_door.rect.bottom
                entity.velY = 0
                entity.collision_types['top'] = True
        else:
            if collide_door.velX < 0 and entity.rect.top < collide_door.rect.top:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = -.1
                entity.collision_types['bottom'] = True
            elif collide_door.velX > 0 and entity.rect.top < collide_door.rect.top:
                entity.rect.bottom = collide_door.rect.top
                entity.velY = .1
                entity.collision_types['bottom'] = True
            print(collide_door.rect.top, entity.rect.top - (entity.rect.height/2))
            if collide_door.rect.top < entity.rect.bottom - (entity.rect.height/2):
                entity.dead = True
                entity.color = (100, 100, 100)
            if collide_door.rect.bottom < entity.rect.top - (entity.rect.height/2):
                entity.dead = True
                entity.color = (100, 100, 100)


