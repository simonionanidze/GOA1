def rgb_to_grey(r, g, b):
    
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    
    return round(gray)
