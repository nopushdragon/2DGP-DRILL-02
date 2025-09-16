from idlelib.multicall import MC_ENTER

from pico2d import *
import os
import math
os.chdir('C:\\Users\\User\Documents\GitHub\\2DGP-DRILL-02')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while (1):
    while (x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)
    while(y < 555):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.001)
    while (x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.001)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.001)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.001)
    angle = 0
    r = 233
    while(angle > -360 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        angleradian = math.radians(angle-90)
        x = 400+r*math.cos(angleradian)
        y = 322+r*math.sin(angleradian)
        character.draw_now(x, y)
        angle = angle - 1
        delay(0.001)

close_canvas()