from FractalWorld import *
height1=1000
width1=1500
w = FractalWorld(width=width1,height=height1,delay=0.01) #creates our world, with some arguments for height, width and delay
f = Fractal(draw=True) #creates a Fractal, which is the same as a turtle in turtleworld, except here itself isn't drawn.
f.x = -(width1/2)+50 # sets the newly created Fractal's x-posistion to 50 pixels to the right of the left border of the window.
f.y = -(height1/2)+50 # sets the Fractal's y-posistion to 50 pixels above the lower border of the window.

def sierp(f,s,d):
  """
  Draws a Sierpinski Triangle with a sidelength of s/2 of depth d with the fractal
  or turtle f.
  """
  if d == 0:
    pd(f)
    fd(f,s)
  else:
    sierp(f,s/2,d-1)
    lt(f,120)
    sierp(f,s/2,d-1)
    lt(f,120)
    sierp(f,s/2,d-1)
    lt(f,120)
    pu(f)
    fd(f,s)

sierp(f,2048,5)
w.wait_for_user()
