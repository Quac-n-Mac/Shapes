import pgzrun
WIDTH = 750
HEIGHT = 750



def draw():
    w = 750
    h = 50

    r = 2
    g = 10
    b = 5
    screen.fill("black")
    # screen.draw.filled_rect(rec,(255,0,0))
    for i in range(5):
        rec = Rect((0,0),(w,h))
        rec.center = 375, 375 
        screen.draw.rect(rec, (r,g,b))
        w = w * 0.5
        h = h * 1.5
        r = r + 5
        g = g - 3
        b = b - 1
def update():
    pass
pgzrun.go()