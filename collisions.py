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
            pos_height = 25 - rel_x
        pos_height = min(pos_height, 25)
        pos_height = max(pos_height, 0)
        target_y = collide_ramp.rect.y + 25 - pos_height
        if collide_ramp.typ == "RampR" and rel_x > 15 and entity.velX < 0:
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
            if entity.velX == 0 and collide_ramp.typ == "RampR" and rel_x < 25:
                entity.velX = -.1
                entity.velY = -.1
            if entity.velX == 0 and collide_ramp.typ == "RampL":
                entity.velX = .1
                entity.velY = -.1
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
            entity.color = (100, 100, 100)
        elif entity.name == "flow" and collide_fluid.typ == "electricity":
            entity.color = (100, 100, 100)
        elif collide_fluid.typ == "acid":
            entity.color = (100, 100, 100)
