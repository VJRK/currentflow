def clamp(value, max_value, min_value):
    if value > max_value:
        value = max_value
    elif value < min_value:
        value = min_value
    return value
