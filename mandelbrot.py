import numpy as np
import colorsys
from pylab import imshow, show

def mandelbrot_iters(real, img, max_iters=20):
  """
    Returns the number of iterations it takes to diverge.
  """
  c = complex(real, img)
  z = 0.0j
  for i in range(max_iters):
    z = z*z + c
    if abs(z) >= 4:
      return i

  return max_iters


def render_mandelbrot(min_x, max_x, min_y, max_y, image, max_iters=20):
    assert(max_x > min_x)
    assert(max_y > min_y)
    pixel_width = (max_x - min_x) / width
    pixel_height = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_width
        for y in range(height):
            img = min_y + y * pixel_height
            iters = mandelbrot_iters(real, img, max_iters)
            # hsv = [round(i * 255) for i in colorsys.hsv_to_rgb(iters / max_iters,0.5,1)]
            # color = [hsv[2], hsv[1], hsv[0]]
            # print(color)
            image[y, x] = iters

if __name__ == '__main__':
    height = 1080
    width = 1920

    img = np.zeros((height,width ), dtype = np.uint8)
    render_mandelbrot(-2, 1, -1, 1, img)
    imshow(img)
    show()