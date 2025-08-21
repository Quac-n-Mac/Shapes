import pgzrun
import random

WIDTH = 900
HEIGHT = 900

def draw():
    screen.fill("black")
    rad = 100
    # screen.draw.circle((450,450), 100, (255,255,255))
    w = 750
    h = 11
    r = 255
    g = 1
    b = 1

    for i in range(30):
        rec = Rect((0,0),(w,h))
        rec.center = 375, 375 
        screen.draw.rect(rec, (r,g,b))
        w = w - random.randint(2,6)
        h = h * random.randint(1,2)
        r = r / random.randint(1,2)
        g = g + random.randint(0,5)
        b = b * 1.2
        screen.draw.circle((w - 5,rad + 20), rad * 0.75, (r,g,b))
        rad = rad + 15
        print("Hi")
# def update():
#     pass
pgzrun.go()