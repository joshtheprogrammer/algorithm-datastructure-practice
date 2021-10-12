rgb = [130, 10, 130]

lowest = 255
for color in rgb:
    if color < lowest:
        lowest = color

rgb[0] -= lowest
rgb[1] -= lowest
rgb[2] -= lowest

print(rgb)

    