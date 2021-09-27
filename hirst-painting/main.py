import colorgram as cg

colors = cg.extract('hirst.jpg',30)
my_colors = []

for i in colors:
    my_colors.append((i.rgb.r,i.rgb.g,i.rgb.b))

print(my_colors)