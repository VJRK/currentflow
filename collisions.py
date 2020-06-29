
def check_collisions(entity, blocks):
    collisions = []
    for block in blocks:
        if entity.colliderect(block.rect):
            collisions.append(block)
    return collisions
