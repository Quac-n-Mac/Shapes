import pgzrun
import random

WIDTH = 600
HEIGHT = 600

messege = "Start the game"
shots = 0
alien = Actor("alien")



alien.pos = random.randint(100,500), random.randint(100,500)       #   alien.x = 300

def draw():
    screen.fill("DarkSeaGreen")
    alien.draw()
    screen.draw.text(messege, center = (475,15), fontsize = 40, color = "blue2")

def on_mouse_down(pos):
    print(pos)
    global shots, messege, alien
    if alien.collidepoint(pos):
        alien.pos = random.randint(100,500), random.randint(100,500)
        shots = shots + 1
        messege = "Alien shot " + str(shots) + " times."
        if shots >= 5:
            alien.image=("alien")
            print("hi")
        elif shots >= 10:
            alien.image=("aliensmall")
        elif shots >= 20:
            alien.image=("aliensmaller")
        elif shots >= 30:
            alien.image=("alientiny")
    else:
        shots = shots - 1
        

pgzrun.go()