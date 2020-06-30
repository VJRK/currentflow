import globalvalues as gv
import copy


def setdimensions(current_w, current_h):
    old_scale = copy.deepcopy(gv.scale)

    ratio = current_w / current_h
    # Bei breiten Bildschirmen
    if ratio > 16 / 9:
        gv.scale = int(current_h/36)
    # Bei hohen Bildschrimen
    elif ratio <= 16 / 9:
        gv.scale = int(current_w/64)

    gv.gravity = (gv.gravity/old_scale) * gv.scale
    gv.jump_speed = (gv.jump_speed/old_scale) * gv.scale
    gv.run_acc = (gv.run_acc/old_scale) * gv.scale
    gv.base_run_speed = (gv.base_run_speed/old_scale) * gv.scale
    gv.max_run_speed = (gv.max_run_speed/old_scale) * gv.scale
    gv.slide_speed = (gv.slide_speed/old_scale) * gv.scale  # muss weniger als base_speed sein

"""
def setdimensions(current_w, current_h):
    ratio = current_w / current_h
    # Bei breiten Bildschirmen
    if ratio > 16 / 9:
        gv.width = int(current_h * 16 / 9)
        gv.height = current_h
        gv.L = int((current_w - gv.width) / 2)
        gv.T = 0
    # Bei hohen Bildschrimen
    elif ratio < 16 / 9:
        gv.width = current_w
        gv.height = int(current_w * 9 / 16)
        gv.origin = (0, int((current_h - gv.height) / 2))
        gv.L = 0
        gv.T = int((current_h - gv.height) / 2)
    else:
        gv.width = current_w
        gv.height = current_h
        gv.L = gv.T = 0
    gv.R = gv.L + gv.width
    gv.B = gv.T + gv.height

    gv.scale = gv.width / 1600
    gv.hitbox_cu = (32 * gv.scale, 48 * gv.scale)
    gv.hitbox_fl = (40 * gv.scale, 32 * gv.scale)
"""""
