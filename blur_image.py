import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())


for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # TODO: Randomly choose the coordinates of a neighboring pixel\
        new_x = random.randint(i-1, i+1)
        new_y = random.randint(j-1, j+1)
        
        # TODO: in the new image, set this pixel's color to the neighbor's color
        neighbor_color = img.getPixel(new_x,new_y)
        new_img.setPixel(i, j, neighbor_color)
        
new_img.draw(win)
win.exitonclick()
