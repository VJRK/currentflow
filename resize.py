import globalvalues as gv

resolutions = [(3840, 2160), (3200, 1800), (2560, 1440), (1920, 1080), (1600, 900), (1280, 720), (640, 360)]


def get_resolution_index(current_w, current_h):
    index = 0
    ratio = current_w / current_h
    # Bei breiten Bildschirmen nach der Höhe richten
    if ratio > 16 / 9:
        for res in resolutions:
            if current_h < res[1]:
                index += 1
    else:
        for res in resolutions:
            if current_w < res[0]:
                index += 1
    return index
