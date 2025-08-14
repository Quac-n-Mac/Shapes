import pgzrun

WIDTH = 900
HEIGHT = 900

def draw():
    screen.fill("black")
    rad = 100
    # screen.draw.circle((450,450), 100, (255,255,255))
    for i in range(10):
        screen.draw.circle((450,450), rad, (255,255,255))
        rad = rad + 30

def update():
    pass
pgzrun.go()