from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('painting.jpg', 16)
colors_rgb = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_temp = (r, g, b)

    colors_rgb.append(color_temp)


print(colors_rgb)
