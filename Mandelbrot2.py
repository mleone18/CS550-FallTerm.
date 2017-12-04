import tkinter
from tkinter import *
import colorsys


# recursive mandelbrot function gives us the number of iterations to escape
def mandelbrot(z, c, count):
	z = z*z + c
	#update iteration counter
	count = count + 1

	# if we escape or we hit the max number of iterations
	# stop executing and return the number of iterations
	#if count >= maxIt or zx*zx + zy*zy >= 4:
	if count >= maxIt:
		return count
	elif abs(z) >= 2:
		return count
	# otherwise, since we didn't escape or hit the max iterations,
	# calculate a new z again (call mandelbrot function again)
	else:
		return mandelbrot(z, c, count)

# variables we will use throughout the program
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin =  0.33321
xmax =  0.37196
ymin = 0.33467
ymax = 0.37342
maxIt = 255 # max iterations; corresponds to color

# create a new Tkinter window
window = Tk()

# create a canvas, and place it in the window
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
    for col in range(WIDTH):
    	# calculate C for each pixel
        c = complex((((xmax-xmin)*col)/WIDTH)+ xmin, (((ymax-ymin)*row)/HEIGHT)+ ymin)
        
        # set z to 0
        z = complex(0.0, 0.0)

        # execute the mandelbrot calculation
        r = mandelbrot(z, c, 0)


        # use the mandelbrot result to create a color
        rd = hex(abs(115 - r))[2:].zfill(2)
        

        gr = hex(abs(255-r))[2:].zfill(2)
    

        bl = hex(abs(r))[2:].zfill(2)
    

        # update the pixel at the current position to hold
        # the color we created with the mandelbrot result
   
        img.put("#" + rd + bl + gr, (col, row))

# update the canvas and display our drawing
canvas.pack()
mainloop()
