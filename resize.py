import globalvalues as gv


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

    gv.jumpHeight = 100 * gv.scale
    gv.velXmaxGround = 0.5 * gv.scale
    gv.velXmaxAir = 1000 * gv.scale
    gv.velYmaxUp = -1000 * gv.scale
    gv.velYmaxDown = 10 * gv.scale
    gv.run_acc = 0.005 * gv.scale
