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
        gv.L = 0
        gv.T = int((current_h - gv.height) / 2)
    else:
        gv.width = current_w
        gv.height = current_h
        gv.L = gv.T = 0
    print(gv.width, gv.height)
    print(gv.L, gv.T)
